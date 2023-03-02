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

comando = f'''
SELECT * 
FROM PUBLICA_PRODUTO
WHERE DATATH  > {today_format_Y}
AND FLAG = -9
AND ORIGEM_ID = {origem_id}
'''

df_publicacao_anuncio = pd.read_sql(comando, conexao)

# Limpa Terminal
os.system('cls')

# Confere se tem algúm titulo com caixa alta
codid_maiusculas = set()
preco_zerados = set()
titulos_pequenos = set()

for i in range(len(df_publicacao_anuncio)):
    contador = 0
    titulo = df_publicacao_anuncio['TITULO'][i]
    codid = df_publicacao_anuncio['CODID'][i]
    preco_de = df_publicacao_anuncio['VALOR1'][i]
    preco_por = df_publicacao_anuncio['VALOR2'][i]
    
    # Preço
    if preco_de == 0 or preco_por == 0:
        preco_zerados.add(codid)
    
    # Titulo Pequeno
    titulo_sem_espaco = titulo.strip()
    if len(titulo_sem_espaco) < 80:
        titulos_pequenos.add(codid)
    
    # Titulo Maiuscula
    titulo_splitado = titulo.split(' ')
    for titulo in titulo_splitado:
        if titulo.isupper():
            contador = contador + 1
            if contador == 3:
                codid_maiusculas.add(codid)
    
print('\nTÍTULOS EM MAIÚSCULO: \n')
if len(codid_maiusculas) > 0:
    for codid in codid_maiusculas:
        indice = df_publicacao_anuncio['CODID'].index[df_publicacao_anuncio['CODID'] == codid].tolist()[0]
        titulo = df_publicacao_anuncio['TITULO'][indice]
        print(f'CODID:{codid} - {titulo}')
else:
    print(f'Erros: 0')

print('\nPREÇOS ZERADOS: \n')
if len(preco_zerados) > 0:
    for codid in preco_zerados:
        indice = df_publicacao_anuncio['CODID'].index[df_publicacao_anuncio['CODID'] == codid].tolist()[0]
        print(f'CODID:{codid} - {preco_de}/{preco_por}')
else:
    print(f'Erros: 0')

print('\nTITULOS MENORES QUE 80 CARACTERES:\n')
if len(titulos_pequenos) > 0:
    for codid in titulos_pequenos:
        indice = df_publicacao_anuncio['CODID'].index[df_publicacao_anuncio['CODID'] == codid].tolist()[0]
        print(f'CODID:{codid} - {titulo}')
else:
    print(f'Erros: 0')
