import pandas as pd
import pyodbc
import datetime
import pandas as pd
import warnings
import os
import sys
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import get_connection

os.system('cls')
connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()

now = datetime.datetime.now()
digit_of_hour = str(now.hour)
today = datetime.datetime.today()
today_format_Y = today.strftime("%d-%m-%Y")
today_format_y = str(today.strftime("%d-%m-%y"))
acrescimo_sku = today_format_y.replace('-','')
acrescimo_sku = digit_of_hour + acrescimo_sku

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

# Verifica se já foi adicionado SKU
comando = f'''
SELECT SKU
FROM PUBLICA_PRODUTO
WHERE DATATH > '{today_format_Y}'
AND ORIGEM_ID = '{origem_id}'
'''
df_publica_produto = pd.read_sql(comando, conexao)
listaSKU = df_publica_produto['SKU'].tolist()
listaSKU = [valor.strip() for valor in listaSKU]
result_check = [acrescimo_sku in valor for valor in listaSKU]
if not True in result_check:
    print('correto')

    # Adiciona a substring nos SKUS
    comando = f'''
    UPDATE PUBLICA_PRODUTO
    SET SKU = LEFT(SKU, 30 - 8) + '{acrescimo_sku}'
    WHERE DATATH > '{today_format_Y}'
    AND ORIGEM_ID = '{origem_id}'
    '''
    cursor.execute(comando)
    conexao.commit()

    # Remove os espaços em branco
    comando = f'''
    UPDATE PUBLICA_PRODUTO
    SET SKU = REPLACE(SKU, ' ', '')
    WHERE DATATH > '{today_format_Y}'
    AND ORIGEM_ID = '{origem_id}'
    '''

    cursor.execute(comando)
    conexao.commit()
    print('\nSucesso!')
else:
    print('\nJá existe substring (acrescimo de sku) em algum SKU!')
del conexao