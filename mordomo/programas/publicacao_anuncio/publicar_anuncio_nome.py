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
    
# Preenchendo o campo PAI caso seja 0
comando = '''
SELECT CODID, COD_INTERNO, DESCRICAO, PAI
FROM MATERIAIS
WHERE INATIVO = 'N'
'''
df_materiais = pd.read_sql(comando, conexao)
df_materiais['PAI_COMPLETO'] = np.where(df_materiais['PAI'] == 0, df_materiais['CODID'], df_materiais['PAI'])
df_materiais.drop(['PAI'],axis=1, inplace=True)

# Alterando o nome, pois quero puxar as descricoes dos pais
df_materiais.rename({'CODID':'MATERIAL_ID', 'PAI':'CODID'})

#  Obtendo as descrições apenas dos PAIS com base no preenchimento anterior
comando = '''
SELECT CODID, DESCRITIVO
FROM MATERIAIS
WHERE INATIVO = 'N'
'''
df_materiais_aux = pd.read_sql(comando, conexao)
df_materiais = df_materiais.merge(df_materiais_aux, on='CODID')

# Removendo PAI_COMPLETO pois serviu apenas para junção
df_materiais.drop(['PAI_COMPLETO'], axis=1, inplace=True)


# Obtendo apenas a primeira linha do descritivo
titulos_list = []

for i in range(len(df_materiais)):
    descricao = df_materiais['DESCRITIVO'][i]
    try:
        titulo_descricao = descricao.splitlines()[0]
        titulo_descricao = titulo_descricao.replace('"', '')
        caracteres = len(titulo_descricao)
        titulos_list.append(titulo_descricao)
    except:
        titulos_list.append('NULL')
        
df_materiais['TITULO'] = titulos_list


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
SELECT CODID, TITULO AS TITULO_ANTIGO
FROM PUBLICA_PRODUTO
WHERE DATATH > '{today_format_Y}'
AND ORIGEM_ID = '{origem_id}'
'''

df_publica_produto = pd.read_sql(comando, conexao)

# Juntando tabela publicacao e titulos 
df_publica_produto_com_titulo = df_publica_produto.merge(df_materiais, on='CODID')
df_publica_produto_com_titulo.drop(['DESCRITIVO', 'DESCRICAO'], axis=1, inplace=True)

# Buscando por cada titulo, usando REPLACE para substituir o titulo da descricao
for i in range(len(df_publica_produto_com_titulo)):
    titulo_antigo = df_publica_produto_com_titulo['TITULO_ANTIGO'][i]
    titulo_novo = df_publica_produto_com_titulo['TITULO'][i]
    codid = df_publica_produto_com_titulo['CODID'][i]
    print(f'{str(i)}/{str(len(df_publica_produto_com_titulo))} - CODID:{codid}')
    comando = f'''
    UPDATE PUBLICA_PRODUTO
    SET TITULO = REPLACE(TITULO, '{titulo_antigo}', '{titulo_novo}')
    WHERE CODID = '{codid}'
    AND DATATH > {today_format_Y}
    '''
    cursor.execute(comando)
    conexao.commit()

del conexao