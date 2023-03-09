from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
from PIL import Image
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import win32com.client as win32
from openpyxl.styles import Alignment
import requests
import io
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import openpyxl
from openpyxl.drawing.image import Image
from time import sleep

os.system('cls')
pesquisa = input('\nPesquisa NetShoes: ')
while True:
    quantidade_anuncios = input('Quantidade de anúncios (Max 42): ')
    if quantidade_anuncios.isdigit():
        quantidade_anuncios = int(quantidade_anuncios)
        if quantidade_anuncios <= 42:
            break

print('')
url = f'https://www.netshoes.com.br/busca?nsCat=Natural&q={pesquisa}'
url_mais_vendidos = f'https://www.netshoes.com.br/busca?nsCat=Natural&q={pesquisa}&sort=best-sellers'

user_agent = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/106.0.0.0 Safari/537.36'}

wb = Workbook()
ws = wb.active

titulo_list = []
preco_de_list = []
preco_por_list = []
avaliacoes_list = []
notas_list = []
link_anuncios_list = []
posicao_list = []
link_photos_list = []

page = requests.get(url, headers=user_agent)
site = BeautifulSoup(page.content, "html.parser")

# Obtendo links
container = site.find(class_="item-list")

# Coletando todos links href do atributo a
all_links = [link['href'] for link in container.find_all('a')]

# Filtrando apenas os links que começam com //www.netshoes.com
netshoes_links = [link.replace('//','https://') for link in all_links if link.startswith('//www.netshoes.com')]

# Removendo links que não são de anúncios
for i in range(len(netshoes_links)-1, -1, -1):
    if "//www.netshoes.com.br/busca?" in netshoes_links[i]:
        del netshoes_links[i]

# Entrando em cada link (produto)
for index, link in enumerate(netshoes_links):
    
    if index == quantidade_anuncios:
        break
    
    print(f'{str(index+1)}/{str(quantidade_anuncios)}')
    
    page = requests.get(link, headers=user_agent)
    site = BeautifulSoup(page.content, "html.parser")
    
    container = site.find(id='content')
    
    # Posição do anúncio
    posicao_list.append(index+1)
    
    # Titulo do Anúncio
    title = container.find(class_="short-description").find('h1').getText()
    
    # Nem sempre terá Preço DE
    try:
        preco_de = container.find(class_="reduce").getText().replace('R$ ', '')
    except:
        preco_de = '0'
        
    # Preço Por do Anúncio
    preco_por = container.find('div', class_="default-price").find('strong').getText().replace('R$ ', '')
    
    # Avaliações do Produto
    try:
        container_review = container.find(class_="rating-box")
        avaliacoes = container_review.find('span', class_='rating-box__numberOfReviews').getText().replace(' avaliações', '').replace(' avaliação', '')
        nota = container_review.find(class_='rating-box__value').getText()
    except:
        avaliacoes = '0'
        nota = '0'
        
    # Foto
    link_photo = container.find('img', class_='zoom').get('src')
    
    
    # Append lista
    titulo_list.append(title)
    preco_de_list.append(preco_de)
    preco_por_list.append(preco_por)
    avaliacoes_list.append(avaliacoes)
    notas_list.append(nota)
    link_anuncios_list.append(link)
    link_photos_list.append(link_photo)
    
    os.system('cls')
    print(f'\nPesquisa Netshoes: {pesquisa}\n')

    

# Criar o dicionário
dicionario = {
    "posicao": posicao_list,
    "titulo": titulo_list,
    "preco_de": preco_de_list,
    "preco_por": preco_por_list,
    "avaliacoes": avaliacoes_list,
    "notas": notas_list,
    "link_fotos": link_photos_list,
    "link_anuncios": link_anuncios_list
}

# Criar o dataframe
df = pd.DataFrame(dicionario)

# Converte colunas para float e int
df['preco_de'] = df['preco_de'].str.replace(',','.').astype(float)
df['preco_por'] = df['preco_por'].str.replace(',','.').astype(float)
df['notas'] = df['notas'].str.replace(',','.').astype(float)
df['avaliacoes'] = df['avaliacoes'].astype(int)

# remover substring logo depois da substring '.jpg'
df['link_fotos'] = df['link_fotos'].str.replace(r'\.jpg.*', '.jpg', regex=True)


# Carregue o arquivo Excel
workbook = openpyxl.Workbook()

# Selecione a planilha que contém os dados
worksheet = workbook.active

# Copie os dados do dataframe para a planilha
for r in dataframe_to_rows(df, index=False, header=True):
    worksheet.append(r)

os.system('cls')
print('\nCarregando imagens na planilha...\n')

# Percorra a coluna contendo os links de imagem
for row in worksheet.iter_rows(min_row=2, min_col=7, max_col=7):
    for cell in row:
        # Obtenha o link da imagem da célula
        link = cell.value
        # Se o link estiver vazio, pule para a próxima célula
        if not link:
            continue
        # Baixe a imagem do link usando requests
        response = requests.get(link)
        # Verifique se o download foi bem-sucedido
        if response.status_code != 200:
            print(f"Erro ao baixar a imagem: {response.status_code}")
            continue
        # Crie um objeto Image a partir do conteúdo da imagem
        image = Image(io.BytesIO(response.content))
        # Ajuste o tamanho da imagem para caber na célula
        column_width = worksheet.column_dimensions[cell.column_letter].width
        if column_width is None:
            column_width = 10 # Largura padrão de 10 para colunas não definidas
        row_height = worksheet.row_dimensions[cell.row].height
        if row_height is None:
            row_height = 20 # Altura padrão de 20 para linhas não definidas
        image.width = 8 * (column_width - 2)
        image.height = 7 * (row_height - 2)
        # Adicione a imagem à célula e ajuste o estilo da célula
        worksheet.add_image(image, cell.coordinate)
        cell.alignment = Alignment(wrapText=True, vertical='top')
        cell.value = None

# Adiicona um filtro na primeira linha
worksheet.auto_filter.ref = 'A1:H1'

# ajusta a largura da coluna B para o tamanho máximo do conteúdo
worksheet.column_dimensions['B'].width = 80

# Aumentando o tamanho das linhas
# itera sobre todas as linhas e define a altura desejada
aux = 0
for row in worksheet.rows:
    # Pula o cabeçalho
    if aux != 0:
        row_height = 97.5
        row_dimensions = worksheet.row_dimensions[row[0].row]
        row_dimensions.height = row_height
    aux = aux + 1

# Salve as alterações no arquivo Excel
pesquisa = pesquisa.replace(' ', '-')
workbook.save(f'C:/workspace/cadastro-aton/mordomo/programas/excel/pesquisa-netshoes-{pesquisa}.xlsx')

# Aguarde delay
os.system('cls')
print('Aguarde o delay de 4 segundos.\n')
for i in range(4):
    print(str(i+1))
    sleep(1)

os.system('cls')
print('\nFIM!\n')

# Abrindo excel
caminho_arquivo = f'C:/workspace/cadastro-aton/mordomo/programas/excel/pesquisa-netshoes-{pesquisa}.xlsx'
workbook = openpyxl.load_workbook(filename=caminho_arquivo)

# Cria uma instância do aplicativo Excel
excel = win32.gencache.EnsureDispatch('Excel.Application')

# Abre o arquivo do Excel usando o aplicativo Excel
excel.Workbooks.Open(caminho_arquivo)

# Exibe o aplicativo do Excel na tela
excel.Visible = True