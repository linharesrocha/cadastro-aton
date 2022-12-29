from pathlib import Path
from dotenv import load_dotenv
import os
import pandas as pd
import pyodbc

env_path_sql = Path('.') / '.env-sql'
load_dotenv(dotenv_path=env_path_sql)
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
print("Conexão com o Banco de Dados Bem Sucedida!")

comando = f'''
    SELECT *
    FROM MATERIAIS
    '''

dados = pd.read_sql(comando, conexao)
tamanho_planilha = len(dados)


dados.to_excel('tests.xls', index=False)