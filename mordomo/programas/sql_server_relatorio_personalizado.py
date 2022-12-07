import os
from pathlib import Path

import pyodbc
import pandas as pd
import warnings
import datetime
from dotenv import load_dotenv

date_30 = datetime.datetime.now() - datetime.timedelta(30)
date_90 = datetime.datetime.now() - datetime.timedelta(90)

warnings.filterwarnings('ignore')

env_path = Path('.') / '.env-sql'
load_dotenv(dotenv_path=env_path)
DATABASE=os.environ['DATABASE']
UID=os.environ['UID']
PWD=os.environ['PWD']

dados_conexao = ("Driver={SQL Server};"
            "Server=erp.ambarxcall.com.br;"
            "Database=AmbarDagg;"
            "UID=dagg;"
            "PWD=dagg*123;")


conexao = pyodbc.connect(dados_conexao)
print("Conexão com o Banco de Dados Bem Sucedida!")

cursor = conexao.cursor()

print('Primeiro SQL')
comando = '''
SELECT
A.VLR_SITE2, A.VLR_SITE1, A.PRODMKTP_ID, A.SKU, A.SKUVARIACAO_MASTER, A.ATIVO,
B.CODID, B.COD_INTERNO,  B.DESCRICAO, B.VLR_CUSTO,
C.ESTOQUE,
D.ORIGEM_NOME, GRUPO,
E.DESCRICAO
FROM ECOM_SKU A
LEFT JOIN MATERIAIS B ON A.MATERIAL_ID = B.CODID
LEFT JOIN ESTOQUE_MATERIAIS C ON B.CODID = C.MATERIAL_ID
LEFT JOIN ECOM_ORIGEM D ON A.ORIGEM_ID = D.ORIGEM_ID
LEFT JOIN GRUPO E ON B.GRUPO = E.CODIGO
WHERE C.ARMAZEM = 1
ORDER BY CODID
'''

data = pd.read_sql(comando, conexao)

# Replace Null na coluna ATIVO por 'N'
data['ATIVO'].fillna('N', inplace=True)


print('Segundo SQL')
comando = '''
SELECT A.PEDIDO, A.COD_INTERNO, A.QUANT, B.DATA
FROM PEDIDO_MATERIAIS_ITENS_CLIENTE A
LEFT JOIN PEDIDO_MATERIAIS_CLIENTE B ON A.PEDIDO = B.PEDIDO
'''

# Lendo o SQL
data_h = pd.read_sql(comando, conexao)

# Removendo coluna pois só serviu para o JOIN SQL
data_h.drop('PEDIDO', axis=1, inplace=True)

print('Fazendo Groupby')
# Fazendo o Groupby de 90 e 30 dias
data_h_30 = data_h[(data_h['DATA'] > date_30)]
data_h_30 = data_h_30.groupby('COD_INTERNO').sum()
data_h_30 = data_h_30.reset_index()

data_h_90 = data_h[(data_h['DATA'] > date_90)]
data_h_90 = data_h_90.groupby('COD_INTERNO').sum()
data_h_90 = data_h_90.reset_index()

print('Fazendo Merge')
# Fazendo merge
data_completo = pd.merge(data, data_h_30, on=['COD_INTERNO'], how='left')
data_completo = pd.merge(data_completo, data_h_90, on=['COD_INTERNO'], how='left')

data_completo = data_completo.rename(columns={'QUANT_x': 'QNTD_VENDAS_30', 'QUANT_y': 'QNTD_VENDAS_90'})
data_completo['QNTD_VENDAS_30'].fillna(0, inplace=True)
data_completo['QNTD_VENDAS_90'].fillna(0, inplace=True)

data_completo = data_completo[['CODID', 'COD_INTERNO', 'SKU', 'SKUVARIACAO_MASTER',
             'PRODMKTP_ID', 'DESCRICAO', 'GRUPO', 'VLR_CUSTO',
             'ESTOQUE', 'QNTD_VENDAS_30', 'QNTD_VENDAS_90','ATIVO', 'ORIGEM_NOME', 'VLR_SITE2', 'VLR_SITE1']]


data_completo.to_excel('Relatorio-Personalizado.xls', index=False)
print('Relatório Gerado!')