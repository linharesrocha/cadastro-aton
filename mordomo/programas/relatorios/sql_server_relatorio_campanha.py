import os
from pathlib import Path
import pyodbc
import pandas as pd
import warnings
from datetime import datetime, date, timedelta
from dotenv import load_dotenv
from colorama import *

os.system('cls')

today = date.today()

dt = date.today()
datetime_midnight = datetime.combine(dt, datetime.min.time())
date_30 = datetime_midnight - timedelta(30)
print('\n30 Dias: ' + str(date_30.strftime("%d-%m-%Y")))
date_90 = datetime_midnight - timedelta(90)
print('90 Dias: ' + str(date_90.strftime("%d-%m-%Y")))
print(Fore.YELLOW, '\nCarregando...')
warnings.filterwarnings('ignore')

env_path = Path('.') / 'C:\workspace\cadastro-aton\mordomo\programas\.env-sql'
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

comando = '''
SELECT DISTINCT
A.AUTOID, A.VLR_SITE2, A.VLR_SITE1, A.PRODMKTP_ID, A.SKU, A.SKUVARIACAO_MASTER, A.ATIVO, A.TIPO_ANUNCIO, A.ORIGEM_ID,
B.INATIVO, B.CODID, B.COD_INTERNO,  B.PAI,B.DESCRICAO, B.VLR_CUSTO, B.PESO, B.COMPRIMENTO, B.LARGURA, B.ALTURA,
C.ESTOQUE, 
D.ORIGEM_NOME,
E.DESCRICAO AS GRUPO,
F.CATEG_MKTP_DESC AS DESCRICAON02, F.PRODUTO_TIPO, F.API,
G.CATEG_ID, G.CATEG_NOME
FROM ECOM_SKU A
LEFT JOIN MATERIAIS B ON A.MATERIAL_ID = B.CODID
LEFT JOIN ESTOQUE_MATERIAIS C ON B.CODID = C.MATERIAL_ID
LEFT JOIN ECOM_ORIGEM D ON A.ORIGEM_ID = D.ORIGEM_ID
LEFT JOIN GRUPO E ON B.GRUPO = E.CODIGO
LEFT JOIN CATEGORIAS_MKTP F  ON F.CATEG_ATON = B.ECOM_CATEGORIA AND F.API = D.API
LEFT JOIN ECOM_CATEGORIAS G ON G.CATEG_ID = B.ECOM_CATEGORIA
WHERE C.ARMAZEM = 1
AND B.INATIVO = 'N'
ORDER BY CODID
'''
data = pd.read_sql(comando, conexao)

# Cria nova coluca com os valores da coluna SKU
data['SKU_MESCLADO'] = data['SKU']

# Preenche todos os valores vazios na coluna SKUVARIACAO_MASTER com o valor da mesma linha da coluna SKU
data['SKUVARIACAO_MASTER'].fillna(data['SKU'], inplace=True)
linhas_vazias = data.loc[data['SKUVARIACAO_MASTER'] == '']
data.loc[linhas_vazias.index, 'SKUVARIACAO_MASTER'] = linhas_vazias['SKU']

# Passa para a coluna SKU_MESCLADO os valores de SKUVARIACAO_MASTER (ML, Shopee, B2W, Tray, Decathlon)
data.loc[data['ORIGEM_ID'].isin([8,9,10,11,12,13,17,18,19,32,33]), 'SKU_MESCLADO'] = data['SKUVARIACAO_MASTER']

# Juntar código pai
comando = '''
SELECT COD_INTERNO AS PAI_COD_INTERNO, CODID AS PAI FROM MATERIAIS
WHERE PAI = '0'
'''
data_pai_aux = pd.read_sql(comando, conexao)
data = pd.merge(data, data_pai_aux, on=['PAI'], how='left')
data['PAI_COD_INTERNO'].fillna(data['COD_INTERNO'], inplace=True)

# Juntar categoria pai da Magalu
comando = '''
SELECT A.IDNIVEL01, B.IDNIVEL02, A.API, A.DESCRICAON01, B.DESCRICAON02
FROM ECOM_CATEGORIAN01 A
LEFT JOIN ECOM_CATEGORIAN02 B
ON A.IDNIVEL01 = B.IDNIVEL01
'''
data_categoria_magalu_tmp = pd.read_sql(comando, conexao)
data_categoria_magalu_tmp['API'] = data_categoria_magalu_tmp['API'].str.strip()
data_categoria_magalu_tmp['API'].replace('Integra', 'IntegraCommerce', inplace=True)
data = pd.merge(data, data_categoria_magalu_tmp, on=['DESCRICAON02', 'API'], how='left')
data.rename(columns = {'DESCRICAON02':'CATEGORIAS'}, inplace=True)

comando = '''
SELECT A.PEDIDO, A.COD_INTERNO, A.QUANT, A.COD_PEDIDO AS SKU, A.EDICAO AS SKU2, B.ORIGEM AS ORIGEM_ID, B.DATA
FROM PEDIDO_MATERIAIS_ITENS_CLIENTE A
LEFT JOIN PEDIDO_MATERIAIS_CLIENTE B
ON A.PEDIDO = B.PEDIDO
WHERE B.TIPO = 'PEDIDO'
AND B.POSICAO != 'CANCELADO'
'''

# Preenchendo pedidos
data_h = pd.read_sql(comando, conexao)
data_h.drop('PEDIDO', axis=1, inplace=True)
data_h_aux = data_h[(data_h['QUANT'] > 1)]
data_h_aux['QUANT'] = data_h_aux['QUANT'] - 1
for i in range(len(data_h_aux)):
    cod_interno = data_h_aux['COD_INTERNO'].iloc[i]
    quantidade = int(data_h_aux['QUANT'].iloc[i])
    sku = data_h_aux['SKU'].iloc[i]
    sku2 = data_h_aux['SKU2'].iloc[i]
    origem = data_h_aux['ORIGEM_ID'].iloc[i]
    data_venda = data_h_aux['DATA'].iloc[i]
    for j in range(quantidade):
        row1 = pd.Series([cod_interno, 1, sku, sku2, origem, data_venda], index=data_h.columns)
        data_h = data_h.append(row1, ignore_index=True)

# Colocando todos valores da coluna SKU2 na coluna SKU da Dafiti
data_h.loc[data_h['ORIGEM_ID'].isin([5,6,7]), 'SKU'] = data_h['SKU2'].fillna(data_h['SKU'])

# VENDAS ATON (COD INTERNO)
# Fazendo o Groupby de 90 e 30 dias
data_h_30 = data_h[(data_h['DATA'] >= date_30)]
data_h_30 = data_h_30.groupby('COD_INTERNO').count()
data_h_30 = data_h_30.reset_index()
data_h_30.drop(['SKU', 'DATA'], axis=1, inplace=True)

data_h_90 = data_h[(data_h['DATA'] >= date_90)]
data_h_90 = data_h_90.groupby('COD_INTERNO').count()
data_h_90 = data_h_90.reset_index()
data_h_90.drop(['SKU', 'DATA'], axis=1, inplace=True)

# Fazendo merge
data_completo = pd.merge(data, data_h_30, on=['COD_INTERNO'], how='left')
data_completo = pd.merge(data_completo, data_h_90, on=['COD_INTERNO'], how='left')

# Renomeando colunas
data_completo.drop(columns=['ORIGEM_ID'], axis=1, inplace=True)
data_completo = data_completo.rename(columns={'QUANT_x': '30_ATON', 'QUANT_y': '90_ATON', 'VLR_SITE1': 'PRECO_DE', 'VLR_SITE2': 'PRECO_POR', 'ORIGEM_ID_x':'ORIGEM_ID'})

# Colocando valor Zero para aqueles produtos Aton que não tiveram vendas
data_completo['30_ATON'].fillna(0, inplace=True)
data_completo['90_ATON'].fillna(0, inplace=True)

# Colocando horário
data_completo['HORARIO'] = datetime.now()

# Marketplace
data_completo['30_MKTP'] = 'MANUTENCAO'
data_completo['90_MKTP'] = 'MANUTENCAO'

# VENDAS MARKETPLACE (SKU ANÚNCIO)
# Fazendo o Groupby de 90 e 30 dias
data_h_30_mktp = data_h[(data_h['DATA'] >= date_30)]
data_h_30_mktp['SKU_MESCLADO'] = data_h_30_mktp.apply(lambda x: x['SKU'] if pd.isnull(x['SKU2']) else x['SKU2'], axis=1)
data_h_30_mktp.drop(['SKU', 'SKU2', 'DATA'], axis=1, inplace=True)
data_h_30_mktp = data_h_30_mktp.groupby(['SKU_MESCLADO','ORIGEM_ID']).count()
data_h_30_mktp = data_h_30_mktp.reset_index()
data_h_30_mktp.drop(columns=['COD_INTERNO'], axis=1, inplace=True)

data_completo = pd.merge(data_completo, data_h_30_mktp[['ORIGEM_ID', 'SKU_MESCLADO', 'QUANT']], on=['SKU_MESCLADO', 'ORIGEM_ID'], how='left')

# Preenchendo valores nan por 0
data_completo['QUANT'].fillna(0, inplace=True)

data = data_completo
data = data_completo[['CODID', 'COD_INTERNO', 'PAI_COD_INTERNO', 'SKU', 'SKUVARIACAO_MASTER',
                      'PRODMKTP_ID', 'DESCRICAO', 'GRUPO', 'VLR_CUSTO', 'PESO',
                      'ESTOQUE', '30_ATON', '90_ATON', '30_MKTP', '90_MKTP','ORIGEM_NOME', 'CATEGORIAS', 'PRODUTO_TIPO',
                      'COMPRIMENTO', 'LARGURA', 'ALTURA', 'TIPO_ANUNCIO', 'CATEG_ID', 'CATEG_NOME',
                      'PRECO_DE', 'PRECO_POR', 'HORARIO', 
                      'QUANT', 'ORIGEM_ID']]

# Obtenha os nomes das colunas de cada DataFrame como conjuntos
cols1 = set(data_completo.columns)
cols2 = set(data.columns)
diff_cols1 = cols1 - cols2
print('Colunas filtradas (não excluidas, apenas filtradas)')
print(diff_cols1)


# Removendo espaços em branco
data['COD_INTERNO'] = data['COD_INTERNO'].str.strip()
data['DESCRICAO'] = data['DESCRICAO'].str.strip()
data['ORIGEM_NOME'] = data['ORIGEM_NOME'].str.strip()
data['SKU'] = data['SKU'].str.strip()

dia_atual = str(today.strftime("%Y-%m-%d"))
agora_hora = datetime.now()
horal_atual = str(agora_hora.strftime("%H:%M:%S")).replace(':','-')

# data.to_excel('C:\workspace\cadastro-aton\mordomo\programas\excel\Planilha-de-Campanha-'+ str(d1) + '.xls', index=False)
data.to_excel(f'C:\workspace\cadastro-aton\mordomo\programas\excel\Planilha-de-Campanha-{dia_atual}-{horal_atual}.xlsx', index=False, encoding='utf-8')
print(Fore.GREEN,'\nRelatório Gerado!')