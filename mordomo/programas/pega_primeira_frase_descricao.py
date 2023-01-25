import os
from pathlib import Path
import pyodbc
import pandas as pd
import warnings
from datetime import datetime, date, timedelta
from dotenv import load_dotenv


warnings.filterwarnings('ignore')
env_path = Path('.') / '.env-sql'
load_dotenv(dotenv_path=env_path)
DATABASE = os.environ['DATABASE']
UID = os.environ['UID']
PWD = os.environ['PWD']

dados_conexao = ("Driver={SQL Server};"
                 "Server=erp.ambarxcall.com.br;"
                 "Database=" + DATABASE + ";"
                                          "UID=" + UID + ";"
                                                         "PWD=" + PWD + ";")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()
comando = '''
SELECT CODID, COD_INTERNO, DESCRICAO, DESCRITIVO
FROM MATERIAIS
WHERE INATIVO = 'N'
AND DESCRITIVO IS NOT NULL
'''

data = pd.read_sql(comando, conexao)
descritivo_lista = data['DESCRITIVO'].tolist()
primeiro_nome = []

for descritivo in descritivo_lista:
    aux = 0
    titulo_descricao = descritivo.splitlines()[0]
    primeiro_nome.append(titulo_descricao)
    titulo_separado = titulo_descricao.split(' ')


data['PRIMEIRO_NOME'] = primeiro_nome
data.to_excel('primeiro_nome.xls', index=False)
