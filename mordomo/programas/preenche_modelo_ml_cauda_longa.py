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


data = pd.read_excel('excel/primeiro_nome_com_60.xls')


for i in range(len(data)):
    codid = data['CODID'][i]
    valor = data['DIFERENCA'][i]
    print(f'CODID: {codid} -- VALUE: {valor}')
    cursor.execute(f'''
                    UPDATE MATERIAIS_ESPECIFICACOES
                    SET VALOR = '{valor}'
                    WHERE API = 'Mercado Livre'
                    AND TIPO = 'Modelo'
                    AND IDTIPO = 'MODEL'
                    AND CODID = '{codid}'
                    ''')

    conexao.commit()
    print(' ')