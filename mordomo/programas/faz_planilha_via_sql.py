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
SELECT MATERIAL_ID AS CODID, PRODMKTP_ID,VLR_SITE1, VLR_SITE2, TITULO, ESTOQUE, ATIVO, EXISTE
FROM ECOM_SKU
WHERE ORIGEM_ID = '25'
'''

data = pd.read_sql(comando, conexao)
data.to_excel('excel/vinculacoes_magalu_pisste.xls', index=False)