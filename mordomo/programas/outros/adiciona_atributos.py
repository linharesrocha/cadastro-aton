import pandas as pd
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
data = pd.read_excel('excel/PREENCHER_ATRIBUTOS_COR_OU_SIZE.xlsx')


for i in range(len(data)):
    break
    codid = data['CODID'].iloc[i]
    atributo = data['FALTANTES'].iloc[i]
    if atributo == 'Cor':
        atributoid = 'COLOR'  
    else: 
        atributoid = 'SIZE'
    print(str(i) + '/' + str(len(data)))
    print(f'{codid} / {atributo} / {atributoid}')
    comando = f'''INSERT INTO MATERIAIS_ESPECIFICACOES(CODID, TIPO, VALOR,PRODUTO, SKU, API, IDTIPO, ALLOW_VARIATIONS, VALOR_ID) VALUES ('{codid}', '{atributo}', '', 'N', 'N', 'Mercado Livre', '{atributoid}', 'S', '')'''
    cursor.execute(comando)
    conexao.commit()

del conexao