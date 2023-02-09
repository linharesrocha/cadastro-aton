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
df_planilha_precos = pd.read_excel('C:\workspace\cadastro-aton\mordomo\programas\excel\Envios_Magalu_Madz_Pisste_Leal.xlsx')
df_publica_produto_com_precos_novos = df_publica_produto.merge(df_planilha_precos, on='CODID')

# Alterarando ponto para virgula, para gravação de dados no Banco
colunas_ponto = ['PRECO_DE_ANTIGO', 'PRECO_POR_ANTIGO', 'PRECO_POR', 'PRECO_DE']
for col in colunas_ponto:
    # Converte o ponto para vírgula e com apenas duas casas decimais
    df_publica_produto_com_precos_novos[col] = df_publica_produto_com_precos_novos[col].apply(lambda x: "{:,.2f}".format(x).replace('.', ','))

for i in range(len(df_publica_produto_com_precos_novos)):
    
    break