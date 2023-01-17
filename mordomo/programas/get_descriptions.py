import os
from pathlib import Path
import pyodbc
import pandas as pd
import warnings
from datetime import datetime, date, timedelta
from dotenv import load_dotenv

warnings.filterwarnings('ignore')
env_path = Path('.') / '.env-sql'
load_dotenv(dotenv_path=env_path)
DATABASE = os.environ['DATABASE']
UID = os.environ['UID']
PWD = os.environ['PWD']

today = date.today()

dt = date.today()
datetime_midnight = datetime.combine(dt, datetime.min.time())
date_30 = datetime_midnight - timedelta(30)
print('Date 30: ' + str(date_30.strftime("%d-%m-%Y")))
date_90 = datetime_midnight - timedelta(90)
print('Date 90: ' + str(date_90.strftime("%d-%m-%Y")))

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
SELECT A.CODID, A.COD_INTERNO, A.DESCRICAO, A.DESCRITIVO, B.ESTOQUE
FROM MATERIAIS A
LEFT JOIN ESTOQUE_MATERIAIS B
ON A.CODID = B.MATERIAL_ID
WHERE INATIVO = 'N'
AND A.DESMEMBRA = 'N'
AND A.COD_INTERNO NOT LIKE 'GO%'
AND B.ARMAZEM = 1
'''

data = pd.read_sql(comando, conexao)

titulos_list = []
contagem_caracteres_list = []

for i in range(len(data)):
    descricao = data['DESCRITIVO'][i]
    try:
        titulo_descricao = descricao.splitlines()[0]
        titulo_descricao = titulo_descricao.replace('"', '')
        caracteres = len(titulo_descricao)
        titulos_list.append(titulo_descricao)
        contagem_caracteres_list.append(caracteres)
    except:
        titulos_list.append('NULL')
        contagem_caracteres_list.append('NULL')

data['TITULO'] = titulos_list
data['CARACT'] = contagem_caracteres_list



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


print('Fazendo Groupby Aton')
# Fazendo o Groupby de 90 e 30 dias
data_h_90 = data_h[(data_h['DATA'] >= date_90)]
data_h_90 = data_h_90.groupby('COD_INTERNO').count()
data_h_90 = data_h_90.reset_index()
data_h_90.drop(['SKU', 'DATA'], axis=1, inplace=True)

print('Fazendo Merge Aton')
# Fazendo merge
data_completo = pd.merge(data, data_h_90, on=['COD_INTERNO'], how='left')
data_completo = data_completo.rename(
    columns={'QUANT': '90_ATON'})
data_completo['90_ATON'].fillna(0, inplace=True)



data_completo.to_excel('produtos_titulos_caract_vendas.xls', index=False)