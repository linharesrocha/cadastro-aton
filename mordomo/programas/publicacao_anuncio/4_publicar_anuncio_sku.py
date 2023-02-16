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
warnings.filterwarnings('ignore')
connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()

now = datetime.datetime.now()
digit_of_hour = str(now.hour)
digit_of_minute = str(now.minute)
today = datetime.datetime.today()
today_format_Y = today.strftime("%d-%m-%Y")
today_format_y = str(today.strftime("%d-%m-%y"))
acrescimo_sku = today_format_y.replace('-','')
acrescimo_sku = acrescimo_sku + digit_of_hour + digit_of_minute

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

print(f'Data de atualização: {today_format_Y}')

# Verifica se já foi adicionado SKU
comando = f'''
SELECT SKU
FROM PUBLICA_PRODUTO
WHERE DATATH > '{today_format_Y}'
AND ORIGEM_ID = '{origem_id}'
AND FLAG = '-9'
'''
df_publica_produto = pd.read_sql(comando, conexao)
listaSKU = df_publica_produto['SKU'].tolist()
listaSKU = [valor.strip() for valor in listaSKU]
result_check = [acrescimo_sku in valor for valor in listaSKU]
result_len = [len(valor) for valor in listaSKU]
result_len_check = all(i <= 9 for i in result_len)

if not True in result_check:
    if result_len_check == True:
        # Adiciona a substring nos SKUS
        comando = f'''
        UPDATE PUBLICA_PRODUTO
        SET SKU = LEFT(SKU, 30 - 10) + '{acrescimo_sku}'
        WHERE DATATH > '{today_format_Y}'
        AND ORIGEM_ID = '{origem_id}'
        AND FLAG = '-9'
        '''
        cursor.execute(comando)
        conexao.commit()

        # Remove os espaços em branco
        comando = f'''
        UPDATE PUBLICA_PRODUTO
        SET SKU = REPLACE(SKU, ' ', '')
        WHERE DATATH > '{today_format_Y}'
        AND ORIGEM_ID = '{origem_id}'
        AND FLAG = '-9'
        '''

        cursor.execute(comando)
        conexao.commit()
        print('\nSucesso!\n')
    else:
        print('\nExiste SKUS igual ou acima com 10 caracteres. Vá verificar!\n')
else:
    print('\nJá existe substring (acrescimo de sku) em algum SKU!\n')

del conexao