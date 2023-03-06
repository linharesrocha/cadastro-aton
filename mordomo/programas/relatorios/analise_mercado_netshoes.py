from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
from PIL import Image
import urllib.request
from io import BytesIO
from openpyxl.drawing.image import Image
import numpy as np
from openpyxl import Workbook

pesquisa = 'Tornozeleira'
url = f'https://www.netshoes.com.br/busca?nsCat=Natural&q={pesquisa}&sort=best-sellers'

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
    
    # Para com determinada quantidade de anúncios já coletados.
    if index == 21:
        print('\nNível de anúncios estipulado atingido.\n')
        break
    
    print(f'{str(index+1)}/{str(len(netshoes_links))}')
    
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
        avaliacoes = container_review.find('span', class_='rating-box__numberOfReviews').getText().replace(' avaliações', '').replace(' avaliação')
        nota = container_review.find(class_='rating-box__value').getText()
    except:
        print('entrei')
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

# cria um arquivo xlsx com uma planilha chamada "Produtos"
wb = Workbook()
ws = wb.active
ws.title = "Produtos"

# adiciona o cabeçalho do DataFrame na primeira linha da planilha
header = list(df.columns)
for i, col in enumerate(header):
    cell = ws.cell(row=1, column=i+1)
    cell.value = col

print('Carregando imagens na planilha...\n')

# itera sobre as linhas do DataFrame
for row in df.itertuples(index=False):

    # carrega a imagem da coluna link_fotos
    response = requests.get(row.link_fotos)
    img = Image(BytesIO(response.content))

    # adiciona as informações da linha na planilha
    for i, value in enumerate(row):
        cell = ws.cell(row=ws.max_row+1, column=i+1)
        if i == len(row) - 1:  # se for a coluna link_fotos
            # adiciona a imagem na célula
            img.width = 100
            img.height = 100
            img.anchor = 'B' + str(ws.max_row)
            img.anchor_type = 'oneCell'
            ws.add_image(img)
        else:
            cell.value = value

# parts = image_path.split('.')
# image_path = '.'.join(parts[:-1]) + '.jpg'
# filename = os.path.join(os.path.expanduser("~"), "Downloads", "imagem_marketplace.jpg")
# urllib.request.urlretrieve(image_path, filename)

df.to_excel('produtos.xlsx', index=False)