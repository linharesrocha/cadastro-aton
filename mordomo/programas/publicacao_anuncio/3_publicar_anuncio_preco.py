import pandas as pd
import pyodbc
import datetime
import pandas as pd
import warnings
import numpy as np
import os
import sys
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import get_connection

warnings.filterwarnings('ignore')
os.system('cls')
connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()

def check_date_format(date_string):
    try:
        datetime.datetime.strptime(date_string, '%d-%m')
        return True
    except ValueError:
        return False

while True:
    today_format_Y = input('\nQual a data que foi inserido as publicações?: ')
    if check_date_format(today_format_Y):
        today_format_Y = today_format_Y + '-2023'
        break
    else:
        print(f'{today_format_Y} não está no formato correto: DIA-MÊS. Por favor, tente novamente.')

# Pegando ORIGEM_ID
comando = f'''
SELECT ORIGEM_ID, ORIGEM_NOME
FROM ECOM_ORIGEM
'''

df_ecom_origem = pd.read_sql(comando, conexao)
print(df_ecom_origem.to_string(index=False))

while True:
    origem_id = input('\nQual ORIGEM_ID para filtragem das publicações?: ')
    if origem_id.isdigit():
        num = int(origem_id)
        if num >= 1 and num <= 33:
            break

# Obtem CODID
comando = f'''
SELECT CODID, VALOR1 AS PRECO_DE_ANTIGO, VALOR2 AS PRECO_POR_ANTIGO
FROM PUBLICA_PRODUTO
WHERE DATATH > '{today_format_Y}'
AND ORIGEM_ID = '{origem_id}'
'''

df_publica_produto = pd.read_sql(comando, conexao)
while True:
    file_path = input("\nPor favor, insira o caminho absoluto do arquivo xlsx: ")
    if os.path.exists(file_path) and file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        break
    else:
        print("O caminho absoluto inserido não é válido ou não é um arquivo xlsx. Tente novamente.")
df_planilha_precos = pd.read_excel(file_path)
df_publica_produto_com_precos_novos = df_publica_produto.merge(df_planilha_precos, on='CODID')

# Renomeando DE E POR - BUG
# columns_name = {'PRECO_DE':'AUX', 'PRECO_POR':'PRECO_DE'}
# df_publica_produto_com_precos_novos.rename(columns=columns_name, inplace=True)
# df_publica_produto_com_precos_novos.rename(columns={'AUX':'PRECO_POR'}, inplace=True)

df_publica_produto_com_precos_novos['PRECO_DE'] = df_publica_produto_com_precos_novos['PRECO_DE'].apply(lambda x: "{:.2f}".format(x) if x % 1 != 0 else "{:.0f}".format(x))
df_publica_produto_com_precos_novos['PRECO_POR'] = df_publica_produto_com_precos_novos['PRECO_POR'].apply(lambda x: "{:.2f}".format(x) if x % 1 != 0 else "{:.0f}".format(x))

for i in range(len(df_publica_produto_com_precos_novos)):
    # Coletando as variáveis
    preco_de_novo = df_publica_produto_com_precos_novos['PRECO_DE'][i]
    preco_por_novo = df_publica_produto_com_precos_novos['PRECO_POR'][i]
    codid = df_publica_produto_com_precos_novos['CODID'][i]

    # Printando informações
    print(f'\n{str(i+1)}/{str(len(df_publica_produto_com_precos_novos))} - CODID:{codid}')
    
    # Substitui o PRECO DE
    comando = f'''
    UPDATE PUBLICA_PRODUTO
    SET VALOR1 = '{preco_de_novo}'
    WHERE CODID = '{codid}'
    AND DATATH > '{today_format_Y}'
    AND FLAG = '-9'
    '''
    cursor.execute(comando)
    conexao.commit()
    
    # Substitui o PRECO POR
    comando = f'''
    UPDATE PUBLICA_PRODUTO
    SET VALOR2 = '{preco_por_novo}'
    WHERE CODID = '{codid}'
    AND DATATH > '{today_format_Y}'
    AND FLAG = '-9'
    '''
    print(preco_de_novo)
    print(preco_por_novo)
    cursor.execute(comando)
    conexao.commit()
    
del conexao