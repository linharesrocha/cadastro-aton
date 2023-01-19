import os
import warnings
from pathlib import Path

import pandas as pd
import pyodbc
import slack
from colorama import *
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

cursor = conexao.cursor()

# GET LAST ORDER
comando = f'''
SELECT CODID, COD_INTERNO, DESCRICAO, DESCRITIVO, LEN(CAST(DESCRITIVO AS nvarchar(MAX))) AS CONTAGEM
FROM MATERIAIS
WHERE INATIVO = 'N'
AND DESCRITIVO IS NOT NULL
AND CODID NOT IN(1425,1426)
AND DESMEMBRA = 'N'
'''


df = pd.read_sql(comando, conexao)
df.to_excel('rel_qnt.xls', index=False)