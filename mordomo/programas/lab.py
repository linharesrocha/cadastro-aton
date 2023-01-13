import os
from pathlib import Path
import pyodbc
import warnings
import slack
import pandas as pd
from dotenv import load_dotenv

warnings.filterwarnings('ignore')

# SLACK SETUP
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
app = slack.WebClient(token=os.environ['SLACK_TOKEN'])

env_path_sql = Path('.') / '.env-sql'
load_dotenv(dotenv_path=env_path_sql)
DATABASE=os.environ['DATABASE']
UID=os.environ['UID']
PWD=os.environ['PWD']

dados_conexao = ("Driver={SQL Server};"
            "Server=erp.ambarxcall.com.br;"
            "Database="+DATABASE+";"
            "UID="+UID+";"
            "PWD="+PWD+";")

conexao = pyodbc.connect(dados_conexao)
print("Conexão com o Banco de Dados Bem Sucedida!")
cursor = conexao.cursor()

# GET LAST ORDER
comando = f'''
SELECT A.AUTOID, A.CODID, B.COD_INTERNO, B.DESCRICAO, A.TIPO, A.VALOR, A.API, A.IDTIPO
FROM MATERIAIS_ESPECIFICACOES A
LEFT JOIN MATERIAIS B
ON A.CODID = B.CODID
WHERE API = 'Mercado Livre'
AND IDTIPO = 'GTIN'
AND VALOR LIKE '39%'
'''

df = pd.read_sql(comando, conexao)

list_ean = []
print(len(df))
print('UPDATE MATERIAIS_ESPECIFICACOES')
print('SET VALOR = CASE VALOR')
for i in range(len(df)):
    ean = df['VALOR'][i]
    ean = ean.replace(' ', '')
    list_ean.append(ean)
    ean_updated = '13' + ean[2:]
    print(f'WHEN {ean} THEN {ean_updated}')

print('END')
print('WHERE VALOR IN (', end='')
last_ean = list_ean[-1]
for ean in list_ean:
    if ean == last_ean:
        print(f"'{ean}')", end='')
    else:
        print(f"'{ean}',",end='')

print("\nAND API = 'Mercado Livre'")
print("AND IDTIPO = 'GTIN'")
print(' ' * 3)