import os
import pyodbc
import pandas as pd
import pyautogui as pg
import wget
import urllib
import shutil
import warnings
from time import sleep
import pyperclip

warnings.filterwarnings('ignore')

DATABASE = 'AmbarDagg'
UID = 'dagg'
PWD = 'dagg*123'

dados_conexao = ("Driver={SQL Server};"
                 "Server=erp.ambarxcall.com.br;"
                 "Database=" + DATABASE + ";"
                                          "UID=" + UID + ";"
                                                         "PWD=" + PWD + ";")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# Limpar terminal
os.system('cls')

while True:
    # Criar a pasta C:\Imagens-Lais caso não exista no C: 
    pasta = r'C:\Imagens-Lais'
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    codid_lista = []
    # Perguntar Usuário qual CODID é o produto
    while True:
        codid = input("\nQual é o CODID do produto?: ")
        if codid.isdigit():
            codid = str(codid)
            codid_lista.append(codid)
            
            anwser = input('\nVocê deseja baixar imagens de outro CODID? (S/N): ').lower()
            while True:
                if anwser == 's' or anwser == 'n':
                    break
                else:
                    print('Resposta incorreta.')
            
            if anwser == 'n':
                break
        else:
            print("Código inválido. Por favor, digite um número.")

    
    print('\nBaixando Imagens...\n')
    for codid in codid_lista:
        # Criar a pasta do CODID caso não exista
        pasta_codid = fr'C:\Imagens-Lais\{codid}'
        if not os.path.exists(pasta_codid):
            os.makedirs(pasta_codid)

        # Gere um alerta para a pessoa ir para a tela do produto > imagens
        # print(f'\nVá para o produto com CODID: {codid} na aba Imagens\n')

        # Buscar as imagens no banco de dados
        comando = f'''
        SELECT AUTOID, CODID, URL
        FROM MATERIAIS_IMAGENS
        WHERE CODID = '{codid}'
        '''

        df_imagens = pd.read_sql(comando, conexao)
        if len(df_imagens) == 0:
            print('Esse produto não contém imagem!')

        # Baixar no C:\Imagens-Lais\CODID
        aux = 1 
        digito_coringa = 99
        for i in range(len(df_imagens)):
            
            # Obtendo a imagem
            url = df_imagens['URL'][i]
            
            # Coloca https caso não tenha na url
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'https://' + url
            
            # Baixa a imagem
            try:
                file_name = wget.download(url)
            except:
                file_name = 'image.jpg'
                urllib.request.urlretrieve(url, file_name)

            current_path = os.getcwd()
            print(current_path)
            
            # Renomeia a imagem
            old_name = rf'{current_path}/{file_name}'
            new_name = rf'{current_path}/{codid}_{aux}_{digito_coringa}.jpg'
            os.rename(old_name, new_name)

            src_path = new_name
            dst_path = rf'C:/Imagens-Lais/{codid}/{codid}_{aux}_{digito_coringa}.jpg'
            shutil.move(src_path, dst_path)
            
            aux = aux + 1


        print('\nFotos Baixadas!\n')

        # Remove as imagens do banco de dados
        comando = f'''
        DELETE
        FROM MATERIAIS_IMAGENS
        WHERE CODID = '{codid}'
        '''
        cursor.execute(comando)
        conexao.commit()

    # Abrir o File Explorer com WINDOWS + E entrar na pasta C:\Imagens-Lais\CODID
    pg.hotkey('win', 'e')
    sleep(0.5)
    pg.hotkey('ctrl', 'l')
    sleep(0.5)
    pg.typewrite(rf'C:/Imagens-Lais/')
    pg.press('ENTER')

    os.system('cls')
    
    # Aviso sobre exclusão das imagens
    # print(f'As imagens do CODID:{codid} foram excluidas do sistema!')
    print(f'\nAs imagens foram excluidas do sistema Aton!')
    
    # Aguardar ela fazer as modificações das imagens (esperar input)
    while True:
        anwser = input('\nFaça as modificações necessárias (OK para continuar): ').upper()
        if anwser == 'OK':
            break
        
    os.system('cls')

    # Verificar se o arquivo existe para prosseguir se não, break
    # CTRL + F para buscar a imagem na pesquisa, apertar 2 vezes ENTER para carregar
    # Clica botão de upload
    while True:
        res = input('\nVÁ PARA TELA CONSULTA DE PRODUTOS (S): ').lower()
        if res == 's':
            os.system('cls')
            break
        else:
            print('Tente novamente.')
    
    for codid in codid_lista:
        aux = 1
        
        # Botão Todos
        pg.moveTo(1620, 64)
        pg.click()

        # Busca
        pg.moveTo(477, 60)
        pg.click()

        # Escrever Código ID
        pg.hotkey('ctrl', 'a')
        pg.press('backspace')
        pg.typewrite(str(codid))

        # Botão Consultar
        pg.moveTo(623, 55)
        pg.click()

        # Input Lais
        while True:
            res = input('\nENTRE NO PRODUTO! (S): ').lower()
            if res == 's':
                # Aba Imagem
                pg.moveTo(783, 225)
                pg.click()
                sleep(1)
                break
            else:
                print('Tente novamente.')
        
        os.system('cls')
        print(f'Fazendo UPLOAD de Imagens do CODID: {codid}')
        while True:
            path_file = rf'C:\Imagens-Lais\{codid}\{codid}_{aux}_{digito_coringa}.jpg'
            if os.path.isfile(path_file):
                # FAZ UPLOAD    
                # Clicar no file explorer do Aton
                pg.moveTo(1125, 329)
                pg.click()
                sleep(1)

                # Pressionar CTRL + L para abrir o link de diretório
                pg.hotkey('ctrl', 'l')

                # Colar o caminho C:\Imagens-Lais\CODID depoois dar ENTER
                sleep(0.5)
                pg.typewrite(rf'C:/Imagens-Lais/{codid}')
                
                pg.press('ENTER')

                # Faz a pesquisa do nome
                sleep(2)
                name_file = f'{codid}_{aux}_{digito_coringa}.jpg'
                pyperclip.copy(name_file)
                
                # Abre a pesquisa lateral
                pg.press(['F6', 'F6', 'F6', 'F6'])
                sleep(0.5)
                pg.hotkey('ctrl', 'v')
                
                # Enter
                pg.press('enter')
                sleep(0.5)
                
                # Upload
                pg.moveTo(1258, 331)
                pg.click()
                sleep(2)
                
                aux = aux + 1
            else:
                os.system('cls')
                print('Indo para o próximo produto...')
                
                # Aba cadastro do produto
                pg.moveTo(563, 214)
                pg.click()
                
                # Botão consultar
                pg.moveTo(765, 866)
                pg.click()
                os.system('cls')
                break



    # Mensagem de Fim
    print('\n\nFIM! Vá para o próximo produto!')
    sleep(1.5)
    os.system('cls')