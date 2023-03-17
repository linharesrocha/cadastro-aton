import os
from pathlib import Path
import pyodbc
import pandas as pd
import warnings
from dotenv import load_dotenv
from colorama import *

# Limpando tela
os.system('cls')

# Filtrando Warnings
warnings.filterwarnings('ignore')

# Banco de Dados
env_path = Path('.') / 'C:\workspace\cadastro-aton\mordomo\programas\.env-sql'
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

while True:
    comando = f'''
    SELECT AUTOID, API, CATEG_MKTP_DESC, DEPARTAMENTO, PRODUTO_TIPO, CATEG_NOME, CATEG_ATON
    FROM CATEGORIAS_MKTP A
    LEFT JOIN ECOM_CATEGORIAS B ON A.CATEG_ATON = B.CATEG_ID
    '''

    df_categorias = pd.read_sql(comando, conexao).sort_values(by=['CATEG_ATON', 'API'])

    # Verifica duplicatas nas colunas CATEG_ATON e API
    duplicatas = df_categorias.duplicated(subset=['CATEG_ATON', 'API'], keep=False)

    # Retorna as linhas duplicadas que possuem ambos os valores duplicados
    df_linhas_duplicadas = df_categorias.loc[duplicatas]

    num_linhas_duplicadas = len(df_linhas_duplicadas)
    
    if num_linhas_duplicadas == 0:
        break
    
    print(f'\nLinhas Duplicadas: {num_linhas_duplicadas}\n')
    print(df_linhas_duplicadas)
    print('')


    autoid = input('Digite o AUTOID para exclusão: ')
    comando = f'''
    DELETE FROM CATEGORIAS_MKTP WHERE AUTOID = '{autoid}'
    '''
    cursor.execute(comando)
    conexao.commit()
    
    os.system('cls')