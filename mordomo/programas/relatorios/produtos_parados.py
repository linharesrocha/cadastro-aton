import pandas as pd
import pyodbc
import datetime
import pandas as pd
import warnings
import numpy as np
import os
import sys
from time import sleep
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import get_connection

# Esse código pega o primeiro dia do mês anterior até o dia atual e verifica
# qual produto não teve venda nesse período.
# Retorna um arquivo Excel formatado.

warnings.filterwarnings('ignore')
os.system('cls')
connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()


today = datetime.date.today()
first_day_last_month = datetime.date(today.year, today.month-1, 1)
first_day_last_month_str = first_day_last_month.strftime('%Y-%m-%d')
last_month = datetime.date(today.year, today.month-1, 1)
month_name = last_month.strftime('%B')
print(f'Verificando produtos que não teve venda entre o periodo {first_day_last_month_str} até hoje.')

path_excel = f'C:/workspace/cadastro-aton/mordomo/programas/excel/produtos-sem-venda-{month_name}.xlsx'
writer = pd.ExcelWriter(path_excel, engine='xlsxwriter')


comando = f'''
SELECT DISTINCT A.CODID, A.COD_INTERNO,A.DESCRICAO
FROM MATERIAIS A
LEFT JOIN PEDIDO_MATERIAIS_ITENS_CLIENTE B ON A.CODID = B.CODID
LEFT JOIN PEDIDO_MATERIAIS_CLIENTE C ON B.PEDIDO = C.PEDIDO
WHERE C.DATA NOT BETWEEN '{first_day_last_month_str}' AND GETDATE() OR C.DATA IS NULL
AND A.COD_INTERNO NOT LIKE '%PAI'
AND A.INATIVO = 'N'
ORDER BY CODID
'''

data = pd.read_sql(comando, conexao)
data['CHECK'] = np.nan * np.empty(len(data))

data.to_excel(writer, sheet_name='Planilha1', index=False)
workbook  = writer.book
worksheet = writer.sheets['Planilha1']
worksheet.set_column('C:C', 60)
(max_row, max_col) = data.shape
column_settings = [{'header': column} for column in data.columns]
worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings, 'style': 'Table Style Medium 21'})
writer.close()
print('\nPLANILHA GERADA!\n')