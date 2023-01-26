import os
from pathlib import Path
import pyodbc
import pandas as pd
import warnings
from dotenv import load_dotenv
from colorama import *

lines = []
print(Fore.YELLOW, 'COMANDO:')
while True:
    user_input  = input()
    if user_input  == '':
        break
    else:
        lines.append(user_input  + '\n')
COMANDO = ''.join(lines)

print(Fore.YELLOW, 'NOME DA PLANILHA:')
SHEET_NAME = input('')
SHEET_NAME = SHEET_NAME.replace(' ', '_')
SHEET_NAME = SHEET_NAME.upper()
print(Fore.YELLOW, '\nPROCESSANDO...')
# Excel
writer = pd.ExcelWriter(f'excel/{SHEET_NAME}.xlsx', engine='xlsxwriter')

# Banco de Dados
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

data = pd.read_sql(COMANDO, conexao)
data.to_excel(writer, sheet_name='Planilha1', index=False)

workbook  = writer.book
worksheet = writer.sheets['Planilha1']
(max_row, max_col) = data.shape
column_settings = [{'header': column} for column in data.columns]
worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings, 'style': 'Table Style Medium 21'})
writer.close()
print(Fore.GREEN, 'PLANILHA GERADA!')