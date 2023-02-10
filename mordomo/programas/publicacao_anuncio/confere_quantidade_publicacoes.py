import pandas as pd
import pyodbc
import pandas as pd
import warnings
import datetime
import os
import sys
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

path_excel_marketplace = 'C:/workspace/cadastro-aton/mordomo/programas/excel/63e68956ea67b6d5dacd985f.xlsx'
FLAG = '1'
STATUSCODE = 200
USR = '239' # Usuário
print(f'Configuração: FLAG({1}) - STATUSCODE({STATUSCODE}) - USR({USR})')

def check_date_format(date_string):
    try:
        datetime.datetime.strptime(date_string, '%d-%m')
        return True
    except ValueError:
        return False

while True:
    awnser = input('\nVoce ja passou o path do excel gerado no marketplace? (S): ').lower()
    if awnser == 's':
        break
    else:
        # Para a execução do programa
        print('Passe o caminho na variável "path_excel_marketplace"')
        sys.exit()

while True:
    today_format_Y = input('\nQual a data que foi inserido as publicações?: ')
    if check_date_format(today_format_Y):
        today_format_Y = today_format_Y + '-2023'
        break
    else:
        print(f'{today_format_Y} não está no formato correto: DIA-MÊS. Por favor, tente novamente.')

while True:
    origem_id = input('\nQual ORIGEM_ID para filtragem das publicações?: ')
    if origem_id.isdigit():
        num = int(origem_id)
        if num >= 1 and num <= 33:
            break


comando = f'''
SELECT A.*, B.COD_INTERNO
FROM PUBLICA_PRODUTO A
LEFT JOIN MATERIAIS B
ON A.CODID = B.CODID
WHERE DATATH > '{today_format_Y}'
AND FLAG = '{FLAG}'
AND STATUSCODE >= {STATUSCODE}
AND USR = '{USR}'
AND ORIGEM_ID = '{origem_id}'
AND B.COD_INTERNO NOT LIKE '%PAI'
'''

# Coleta as publicações com sucesso. Status 200
df_publicacoes = pd.read_sql(comando, conexao)

# Remover espaços na coluna SKU 
df_publicacoes['SKU'] = df_publicacoes['SKU'].str.strip()

# Importa planilha para comparação
# Removendo linhas desnecessarias caso seja Magazine Luiza
if int(origem_id) >= 23 and int(origem_id) <= 25:
    df_marketplace = pd.read_excel(path_excel_marketplace, skiprows=[0,1,3])
else:
    df_marketplace = pd.read_excel(path_excel_marketplace)

# Comparar as colunas dos dois Dataframes
df_faltantes_mktp = df_publicacoes[~df_publicacoes['SKU'].isin(df_marketplace['SKU'])]

if len(df_faltantes_mktp) == 0:
    print(f'\nTodos so SKUS da Publicacao ORIGEM {origem_id} da data {today_format_Y} estao na planilha do Marketplace\n')
else:
    print(f'\nHá SKUS faltando na planilha de Marketplace!!\nRelatório: "excel/faltantes-no-marketplace"\n')
    df_faltantes_mktp.to_excel('C:/workspace/cadastro-aton/mordomo/programas/excel/faltantes-no-marketplace.xlsx')
