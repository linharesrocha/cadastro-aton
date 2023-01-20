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
SELECT A.PEDIDO, A.COD_INTERNO, A.DESCRICAOPROD, A.QUANT, A.COD_PEDIDO AS SKU, B.POSICAO
FROM PEDIDO_MATERIAIS_ITENS_CLIENTE A
LEFT JOIN PEDIDO_MATERIAIS_CLIENTE B
ON A.PEDIDO = B.PEDIDO
WHERE B.TIPO = 'PEDIDO'
AND B.ORIGEM = '24'
AND DATA >=  '01-10-2022'
'''

data = pd.read_sql(comando, conexao)
data.to_excel('excel/relatorio_magalu_leal_vendas.xls', index=False)