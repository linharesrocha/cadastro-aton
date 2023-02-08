import sys
import pandas as pd
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import *

connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()


# Tabela ECOM_ORIGEM
comando =f'''
SELECT ORIGEM_ID, ORIGEM_NOME
FROM ECOM_ORIGEM
'''
ecom_origem = pd.read_sql(comando, conexao)
print(ecom_origem['ORIGEM_ID'][7])

# Tabela ECOM_SKU
comando = f'''
SELECT AUTOID, MATERIAL_ID, SKU, ID_SKU, VLR_SITE1, VLR_SITE2, TITULO, TEXTO, ESTOQUE, EAN, ATIVO, EXISTE, ORIGEM_ID
FROM ECOM_SKU
WHERE ORIGEM_ID = {ecom_origem['ORIGEM_ID'][7]}
ORDER BY MATERIAL_ID
'''
ecom_sku = pd.read_sql(comando, conexao)


counts = ecom_sku['MATERIAL_ID'].value_counts()
counts = counts.reset_index()
counts = counts.rename(columns={'index':'CODID', 'MATERIAL_ID':'QntdAnuncios'})
counts.to_excel('ML-MADZ.xlsx', index=False)

