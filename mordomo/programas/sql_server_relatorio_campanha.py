import os
from pathlib import Path
import pyodbc
import pandas as pd
import warnings
from datetime import datetime, date, timedelta
from dotenv import load_dotenv
today = date.today()

dt = date.today()
datetime_midnight = datetime.combine(dt, datetime.min.time())
date_30 = datetime_midnight - timedelta(30)
print('Date 30: ' + str(date_30.strftime("%d-%m-%Y")))
date_90 = datetime_midnight - timedelta(90)
print('Date 90: ' + str(date_90.strftime("%d-%m-%Y")))

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
print("Conexão com o Banco de Dados Bem Sucedida!")

cursor = conexao.cursor()

print('SQL de Produtos Aton e Marketplace')
comando = '''
SELECT 
A.AUTOID, A.VLR_SITE2, A.VLR_SITE1, A.PRODMKTP_ID, A.SKU, A.SKUVARIACAO_MASTER, A.ATIVO, B.INATIVO,
B.CODID, B.COD_INTERNO,  B.DESCRICAO, B.VLR_CUSTO,
C.ESTOQUE, 
D.ORIGEM_NOME,
E.DESCRICAO AS GRUPO,
F.CATEG_MKTP_DESC AS CATEGORIAS, F.DEPARTAMENTO, F.PRODUTO_TIPO
FROM ECOM_SKU A
LEFT JOIN MATERIAIS B ON A.MATERIAL_ID = B.CODID
LEFT JOIN ESTOQUE_MATERIAIS C ON B.CODID = C.MATERIAL_ID
LEFT JOIN ECOM_ORIGEM D ON A.ORIGEM_ID = D.ORIGEM_ID
LEFT JOIN GRUPO E ON B.GRUPO = E.CODIGO
LEFT JOIN CATEGORIAS_MKTP F  ON F.CATEG_ATON = B.ECOM_CATEGORIA AND F.API = D.API
WHERE C.ARMAZEM = 1
AND B.INATIVO = 'N'
ORDER BY CODID
'''

data = pd.read_sql(comando, conexao)

# Replace Null na coluna ATIVO'
# data['ATIVO'].fillna('N_EXISTE', inplace=True)

print('SQL de Pedidos')
comando = '''
SELECT A.PEDIDO, A.COD_INTERNO, A.QUANT, A.COD_PEDIDO AS SKU, B.DATA
FROM PEDIDO_MATERIAIS_ITENS_CLIENTE A
LEFT JOIN PEDIDO_MATERIAIS_CLIENTE B
ON A.PEDIDO = B.PEDIDO
WHERE B.TIPO = 'PEDIDO'
AND B.POSICAO != 'CANCELADO'
'''

# Lendo o SQL
data_h = pd.read_sql(comando, conexao)

# Removendo coluna pois só serviu para o JOIN SQL
data_h.drop('PEDIDO', axis=1, inplace=True)
print('Extraindo quantidades de produto')
# Pegando os códigos interno com mais de 1 quantidade no mesmo pedido, e preenchendo no df original
data_h_aux = data_h[(data_h['QUANT'] > 1)]
data_h_aux['QUANT'] = data_h_aux['QUANT'] - 1
for i in range(len(data_h_aux)):
    cod_interno = data_h_aux['COD_INTERNO'].iloc[i]
    quantidade = int(data_h_aux['QUANT'].iloc[i])
    sku = data_h_aux['SKU'].iloc[i]
    data_venda = data_h_aux['DATA'].iloc[i]
    for j in range(quantidade):
        row1 = pd.Series([cod_interno, 1, sku, data_venda], index=data_h.columns)
        data_h = data_h.append(row1, ignore_index=True)


# Removendo quantidade de COD interno
# data_h.drop('QUANT', axis=1, inplace=True)

print('Fazendo Groupby Aton')
# Fazendo o Groupby de 90 e 30 dias
data_h_30 = data_h[(data_h['DATA'] >= date_30)]
data_h_30 = data_h_30.groupby('COD_INTERNO').count()
data_h_30 = data_h_30.reset_index()
data_h_30.drop(['SKU', 'DATA'], axis=1, inplace=True)

data_h_90 = data_h[(data_h['DATA'] >= date_90)]
data_h_90 = data_h_90.groupby('COD_INTERNO').count()
data_h_90 = data_h_90.reset_index()
data_h_90.drop(['SKU', 'DATA'], axis=1, inplace=True)

print('Fazendo Merge Aton')
# Fazendo merge
data_completo = pd.merge(data, data_h_30, on=['COD_INTERNO'], how='left')
data_completo = pd.merge(data_completo, data_h_90, on=['COD_INTERNO'], how='left')

data_completo = data_completo.rename(
    columns={'QUANT_x': '30_ATON', 'QUANT_y': '90_ATON', 'VLR_SITE2': 'PRECO_DE', 'VLR_SITE1': 'PRECO_POR'})
data_completo['30_ATON'].fillna(0, inplace=True)
data_completo['90_ATON'].fillna(0, inplace=True)

data = data_completo[['AUTOID', 'CODID', 'COD_INTERNO', 'SKU', 'SKUVARIACAO_MASTER',
                      'PRODMKTP_ID', 'DESCRICAO', 'GRUPO', 'VLR_CUSTO',
                      'ESTOQUE', '30_ATON', '90_ATON', 'ATIVO','INATIVO', 'ORIGEM_NOME', 'CATEGORIAS', 'DEPARTAMENTO', 'PRODUTO_TIPO', 'PRECO_POR', 'PRECO_DE']]

print('Fazendo Groupby Marketplace')
# Fazendo o Groupby de 90 e 30 dias
data_h_30_sku = data_h[(data_h['DATA'] >= date_30)]

# CODIGO MISSAO HERE


# print('Fazendo Merge Marketplace')
# Fazendo merge
# data_completo = pd.merge(data, data_h_30_sku, on=['SKU'], how='left')
# data_completo = pd.merge(data_completo, data_h_90_sku, on=['SKU'], how='left')
# data_completo = data_completo.rename(columns={'QUANT_x': '30_MKTP', 'QUANT_y': '90_MKTP'})
# data_completo['30_MKTP'].fillna(0, inplace=True)
# data_completo['90_MKTP'].fillna(0, inplace=True)

# data_completo = data_completo[['AUTOID', 'CODID', 'COD_INTERNO', 'SKU', 'SKUVARIACAO_MASTER',
#                                'PRODMKTP_ID', 'DESCRICAO', 'GRUPO', 'VLR_CUSTO',
#                                'ESTOQUE', '30_ATON', '90_ATON', '30_MKTP', '90_MKTP', 'ATIVO','INATIVO', 'ORIGEM_NOME',
#                                'PRECO_POR', 'PRECO_DE']]


data_completo = data_completo[['AUTOID', 'CODID', 'COD_INTERNO', 'SKU', 'SKUVARIACAO_MASTER',
                               'PRODMKTP_ID', 'DESCRICAO', 'GRUPO', 'VLR_CUSTO',
                               'ESTOQUE', '30_ATON', '90_ATON', 'ATIVO','INATIVO', 'ORIGEM_NOME',
                                'CATEGORIAS', 'DEPARTAMENTO', 'PRODUTO_TIPO',
                               'PRECO_POR', 'PRECO_DE']]

d1 = today.strftime("%d-%m-%Y")
data_completo.to_excel('excel/Planilha-de-Campanha-'+ str(d1) + '.xls', index=False)
print('Relatório Gerado!')
