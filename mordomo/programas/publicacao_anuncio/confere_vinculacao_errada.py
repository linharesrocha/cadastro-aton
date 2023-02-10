import pandas as pd
import pyodbc
import pandas as pd
import warnings
import os
import sys
from colorama import *
from time import sleep
import pyautogui as pg
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import get_connection

warnings.filterwarnings('ignore')
os.system('cls')
connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()


# Verifica se quer olhar tudo (T para tudo) ou um origem_id especifico
while True:
    awnser = input('Qual ORIGEM_ID você quer olhar? (T para tudo): ').lower()
    if awnser != 't':
        if awnser.isdigit():
            awnser = int(awnser)
            if awnser >= 1 and awnser <= 33:
                break
    else:
        break

# Será filtrado o código id caso o usuário digitou um número
if awnser == 't':
    comando = f'''
    SELECT AUTOID, MATERIAL_ID, A.SKU, B.DESCRICAO,TITULO, ORIGEM_ID, A.ATIVO, A.EXISTE
    FROM ECOM_SKU A
    LEFT JOIN MATERIAIS B
    ON A.MATERIAL_ID = B.CODID
    '''
    df_vinculacoes = pd.read_sql(comando, conexao)
else:
    comando = f'''
    SELECT AUTOID, MATERIAL_ID, A.SKU, B.DESCRICAO,TITULO, ORIGEM_ID, A.ATIVO, A.EXISTE
    FROM ECOM_SKU A
    LEFT JOIN MATERIAIS B
    ON A.MATERIAL_ID = B.CODID
    WHERE A.ORIGEM_ID = {awnser}
    '''

    df_vinculacoes = pd.read_sql(comando, conexao)

# Lista para checar se está condizente
check_list = []

# Verifica ID e SKU se são semelhantes
for i in range(len(df_vinculacoes)):
    codid = str(df_vinculacoes['MATERIAL_ID'][i])
    sku = str(df_vinculacoes['SKU'][i])
    autoid = str(df_vinculacoes['AUTOID'][i])
    
    check_list.append('True') if codid in sku else check_list.append('False')
        

# Salva o Dataframe com a coluna CHECK
df_vinculacoes['CHECK'] = check_list
df_vinculacoes.to_excel('C:/workspace/cadastro-aton/mordomo/programas/excel/check-vinculacoes.xlsx')

print('Sucesso!')
    