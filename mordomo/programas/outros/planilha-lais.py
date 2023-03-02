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
SELECT A.CODID, COD_INTERNO, DESCRICAO, PAI, B.ESTOQUE
FROM MATERIAIS A
LEFT JOIN ESTOQUE_MATERIAIS B
ON A.CODID = B.MATERIAL_ID
WHERE A.INATIVO = 'N'
AND B.ARMAZEM = 1
AND A.DESMEMBRA = 'N'
AND A.GRUPO != '7'
'''

data = pd.read_sql(comando, conexao)
data['ESTOQUE_SOMA'] = 0

for i in range(len(data)):
    pai = data['PAI'][i]
    codid = data['CODID'][i]
    
    if pai == 0:
        data.loc[i, 'PAI'] = codid

data.loc[data['COD_INTERNO'].str.contains('PAI'), 'ESTOQUE'] = 0

for indice, id in data['PAI'].iteritems():
    data_aux = data[data['PAI'] == id]
    soma = data_aux['ESTOQUE'].sum()
    data.loc[data['PAI'] == id, 'ESTOQUE_SOMA'] = soma


# data = data.sort_values(['PAI', 'ESTOQUE'], ascending=[True, False])
data = data[~data['COD_INTERNO'].str.contains('PAI')]

data = data.sort_values(['ESTOQUE_SOMA', 'PAI'], ascending=[False,False])

# data.drop(columns=['ESTOQUE_SOMA'], axis=1, inplace=True)

# Removendo pais

data.to_excel('PLANILHA-ORDENACAO-PAI-ESTOQUE.xlsx',index=False)