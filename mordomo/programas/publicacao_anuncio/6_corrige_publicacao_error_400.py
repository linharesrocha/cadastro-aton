import pandas as pd
import pyodbc
import pandas as pd
import warnings
import os
import sys
import datetime
from colorama import *
from time import sleep
import pyautogui as pg
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import get_connection

warnings.filterwarnings('ignore')
os.system('cls')
connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()

def check_date_format(date_string):
    try:
        datetime.datetime.strptime(date_string, '%d-%m')
        return True
    except ValueError:
        return False
    
while True:
    today_format_Y = input('\nQual a data que foi inserido as publicações? (DD/MM): ')
    if check_date_format(today_format_Y):
        today_format_Y = today_format_Y + '-2023'
        break
    else:
        print(f'{today_format_Y} não está no formato correto: DIA-MÊS. Por favor, tente novamente.')
   
while True:
    error_input = input('\nQual erro você deseja pesquisar?: ')
    if len(error_input) > 3:
        error_input = str('%' + error_input + '%')
        break
    else:
        print('Descreva mais!')
# Pega todos os produtos que deram erro
comando = f'''
SELECT AUTOID, AUTOIDPAI, STATUSCODE, RETORNOSTR, SKURETORNO, FLAG, ERRO_API
FROM PUBLICA_PRODUTO
WHERE DATATH > '{today_format_Y}'
AND ERRO_API LIKE '{error_input}'
AND FLAG = '1'
'''

df_erros_id_variacao = pd.read_sql(comando, conexao)

# Pegando o AUTOID de todos os produtos com AUTOIDPAI 0
df_erros_id_variacao_simples = df_erros_id_variacao[df_erros_id_variacao['AUTOIDPAI'] == 0]
autoidsimples_list = df_erros_id_variacao_simples['AUTOID'].tolist()

# Transformando a coluna AUTOIDPAI em um Set e removendo o AUTOIDPAI 0
autoidpai_set = set(df_erros_id_variacao['AUTOIDPAI'])
autoidpai_set.discard(0)

# Confirma se já está na tela?
while True:
    anwser = input('\nVocê já está na tela de Produtos Selecionados? (S): ').lower()
    if anwser == 'sim' or anwser == 's':
        break

# Faz a publicação dos produtos com variações primeiro
print(Fore.LIGHTBLUE_EX, f'\nQuantidades de AUTOIDPAI: {str(len(autoidpai_set))}')
for indice, autoidpai in enumerate(autoidpai_set):
    
    # Traz os filhos
    comando = f'''
    UPDATE PUBLICA_PRODUTO
    SET FLAG = '0'
    WHERE DATATH > '{today_format_Y}'
    AND ERRO_API LIKE '{error_input}'
    AND AUTOIDPAI = '{autoidpai}'
    '''
    
    cursor.execute(comando)
    conexao.commit()
    
    # Traz o pai
    comando = f'''
    UPDATE PUBLICA_PRODUTO
    SET FLAG = '0'
    WHERE DATATH > '{today_format_Y}'
    AND ERRO_API LIKE '{error_input}'
    AND AUTOID = '{autoidpai}'
    '''
    
    cursor.execute(comando)
    conexao.commit()
    
    print(Fore.LIGHTBLUE_EX, f'\n{str(indice)}/{str(len(autoidpai_set))} - AUTOIDPAI:{autoidpai}')
    
    # Aguarda um segundo antes de consultar
    sleep(1)
    
    # Botão Consultar
    pg.moveTo(771, 84)
    pg.click()
    sleep(1)
    
    # Botão Publicar anúncios
    pg.moveTo(1840, 1014)
    pg.click()
    sleep(0.5)

    # Confirmar publicação
    pg.press('enter')
    sleep(0.5)
    
    # Enter Publicar anúncio
    pg.press('enter')
    sleep(0.5)
    
    # Confirma publicação
    pg.press('left')
    pg.press('enter')

    # Botão Publicar anúncios
    pg.moveTo(1840, 1014)
    pg.click()
    sleep(0.5)

    # Botão Consultar
    pg.moveTo(771, 84)
    pg.click()
    sleep(0.5)
    
    for i in range(5):
        print(Fore.GREEN, i + 1)
        sleep(1)
    print(Fore.LIGHTBLUE_EX, f'*' * 50)
    
print(Fore.LIGHTBLUE_EX, f'\nQuantidades de AUTOID: {str(len(autoidsimples_list))}')

# Faz a publicação dos produtos simples
for indice, autoid in enumerate(autoidsimples_list):
    comando = f'''
    UPDATE PUBLICA_PRODUTO
    SET FLAG = '0'
    WHERE DATATH > '{today_format_Y}'
    AND ERRO_API LIKE '{error_input}'
    AND AUTOID = '{autoid}'
    '''
    
    print(Fore.LIGHTBLUE_EX, f'\n{str(indice)}/{str(len(autoidsimples_list))} - AUTOIDPAI:{autoidpai}')
    
    cursor.execute(comando)
    conexao.commit()
    
    # Aguarda um segundo antes de consultar
    sleep(1)
    
    # Botão Consultar
    pg.moveTo(771, 84)
    pg.click()
    sleep(1)
    
    # Botão Publicar anúncios
    pg.moveTo(1840, 1014)
    pg.click()
    sleep(0.5)

    # Confirmar publicação
    pg.press('enter')
    sleep(0.5)
    
    # Enter Publicar anúncio
    pg.press('enter')
    sleep(0.5)
    
    # Confirma publicação
    pg.press('left')
    pg.press('enter')

    # Botão Publicar anúncios
    pg.moveTo(1840, 1014)
    pg.click()
    sleep(0.5)

    # Botão Consultar
    pg.moveTo(771, 84)
    pg.click()
    sleep(0.5)
    
    for i in range(5):
        print(Fore.GREEN, i + 1)
        sleep(1)
    print(Fore.LIGHTBLUE_EX, f'*' * 50)