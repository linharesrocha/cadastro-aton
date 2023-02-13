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

comando = f'''
SELECT CODIGO, DESCRICAO 
FROM GRUPO
'''
df_grupo = pd.read_sql(comando, conexao)
print(df_grupo.to_string(index=False))
# Perguntar ao usuario o grupo dos produtos
while True:
    grupo_id = input('\nQual GRUPO de Produtos será adicionado nas publicações?: ')
    if grupo_id.isdigit():
        num = int(grupo_id)
        if num == 3 or num == 4 or num == 6 or num == 7:
            break

# Pergunta se vai publicar KIT
while True:
    publica_kit = input('\nVai publicar Kit (S/N): ').lower()
    if publica_kit == 's' or publica_kit == 'n':
        break

# Verificar Kit e Puxa tabela MATERIAIS
if publica_kit == 's':
    comando = f'''
    SELECT *
    FROM MATERIAIS
    WHERE INATIVO = 'N'
    AND GRUPO = '{grupo_id}'
    '''
else:
    comando = f'''
    SELECT *
    FROM MATERIAIS
    WHERE INATIVO = 'N'
    AND GRUPO = '{grupo_id}'
    AND DESMEMBRA = 'N'
    '''
df_materiais = pd.read_sql(comando, conexao) 

# Pegando ORIGEM_ID
comando = f'''
SELECT ORIGEM_ID, ORIGEM_NOME
FROM ECOM_ORIGEM
'''
df_ecom_origem = pd.read_sql(comando, conexao)
print('\n\n' + df_ecom_origem.to_string(index=False))
while True:
    origem_id = input('\nPara qual marketplace será publicado?: ')
    if origem_id.isdigit():
        num = int(origem_id)
        if num >= 1 and num <= 33:
            break

# Comando para criar produto na publicação
for i in range(len(df_materiais)):
    codid = df_materiais['CODID'][i]
    cod_interno = df_materiais['COD_INTERNO'][i]
    descricao = df_materiais['DESCRICAO'][i]
    
    # Código para formar o SKU
    check_pai = df_materiais['PAI'][i]
    if check_pai == '0':
        sku = 'P' + str(codid)
    else:
        sku = 'F' + str(codid)

    
    # Inserção de produto
    comando = f'''INSERT INTO PUBLICA_PRODUTO (DATATH, ORIGEM_ID, CODID, SKU, COD_INTERNO, TITULO, ESTOQUE, VALOR1, VALOR2, USR, MAQSYS, STATUSCODE, FLAG, FLAG_VALIDACAO, USR_PUBLICOU, FRETE_GRATIS, OFICIAL_STORE, OFICIAL_STORE_ID, LEVAEAN, CATALOGO_PRODUTO_ID)
    VALUES (CONVERT(datetime, GETDATE(), 120),'{origem_id}', '{codid}', '{sku}', '{cod_interno}','TITULOTEMPORARIO', '1', '10', '10', '239', 'DAGG-005', '0', '-9', '0', '0', 'N', '', '0','S', '')'''
    
    cursor.execute(comando)
    conexao.commit()
    
    print(f'{str(i + 1)}/{str(len(df_materiais))} - {codid} - {cod_interno} - {descricao}')
    if i == 10:
        break

print('\nSucesso!')