import os
from pathlib import Path
import pyodbc
import pandas as pd
import warnings
from dotenv import load_dotenv
from colorama import *


os.system('cls')
lines = []
print(Fore.RED, '\nCOMANDO:')
while True:
    user_input  = input()
    if user_input  == '':
        break
    else:
        lines.append(user_input  + '\n')
COMANDO = ''.join(lines)

print(Fore.RED, '\nNOME DA PLANILHA:')
SHEET_NAME = input('')
SHEET_NAME = SHEET_NAME.replace(' ', '_')
SHEET_NAME = SHEET_NAME.upper()
print(Fore.RED, '\nPROCESSANDO...')
# Excel
path_excel = f'C:/workspace/cadastro-aton/mordomo/programas/excel/{SHEET_NAME}.xlsx'
writer = pd.ExcelWriter(path_excel, engine='xlsxwriter')

# Banco de Dados
warnings.filterwarnings('ignore')
env_path = Path('.') / 'C:/workspace/cadastro-aton/mordomo/programas/.env-sql'
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
print(Fore.GREEN, '\nPLANILHA GERADA!')
print(' ')
print(Fore.RED, '\nREAD_EXCEL:')
print(Fore.BLUE, f"\ndata = pd.read_excel('C:/workspace/cadastro-aton/mordomo/programas/excel/{SHEET_NAME}.xlsx')")
print(Fore.WHITE,'\n')