import pandas as pd
import pyodbc
import pandas as pd
import warnings
import os
import sys
from colorama import *
import unicodedata
from time import sleep
import pyautogui as pg
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import get_connection

warnings.filterwarnings('ignore')
os.system('cls')
connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()
path_excel = f'C:/workspace/cadastro-aton/mordomo/programas/excel/vinculacoes-aton-marketplace.xlsx'
writer = pd.ExcelWriter(path_excel, engine='xlsxwriter')


def remove_acentos(texto):
    texto_sem_acentos = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    return texto_sem_acentos

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
    descricao = str(df_vinculacoes['DESCRICAO'][i]).lower()
    titulo = str(df_vinculacoes['TITULO'][i]).lower()
    descricao = remove_acentos(descricao)
    titulo = remove_acentos(titulo)
    descricao1 = descricao.split(' ')[0]
    titulo1 = titulo.split(' ')[0]

    # ALGORITMO
    # Verifica se existe CODID no SKU - Compara as duas primeiras palavras do TITULO e DESCRICAO 
    
    if codid in sku:
        if titulo1 == descricao1:
            check_list.append('MUITA BAIXA')
        else:
            check_list.append('BAIXA') 
    else:
        if titulo is None or titulo == None or titulo == 'None' or titulo == 'null' or titulo == 'none' or not titulo or len(titulo) == 0 or titulo.strip() == '':
            check_list.append('VAZIO') 
        elif descricao1 == titulo1:
            check_list.append('MEDIA')
        elif descricao1 in titulo:
            check_list.append('MEDIA')
        else:
            check_list.append('MUITO ALTA')
            
        

# Salva o Dataframe com a coluna CHECK
df_vinculacoes['PROBABILIDADE-ERRO'] = check_list
df_vinculacoes.sort_values(by='MATERIAL_ID', inplace=True)
df_vinculacoes.to_excel(writer, sheet_name='Planilha1', index=False)
workbook  = writer.book
worksheet = writer.sheets['Planilha1']
(max_row, max_col) = df_vinculacoes.shape
column_settings = [{'header': column} for column in df_vinculacoes.columns]
worksheet.autofilter(0, 0, max_row, max_col - 1)
writer.close()

print('\nSucesso!\n')
print('Excel salvo! (excel/vinculacoes-aton-marketplace.xlsx)')
print('\nProbabilidade:\nMUITO BAIXA: Caso o CODID estiver presente no SKU e a PRIMEIRA PALAVRA DO TITULO do ATON for a PRIMEIRA PALAVRA DO nome para marketplace.\n\
BAIXA: Caso o CODID estiver presente no SKU e a PRIMEIRA PALAVRA DO TITULO do ATON NÃO for a PRIMEIRA PALAVRA do nome para marketplace.\n\
MEDIA: Caso o CODID NÃO estiver presente no SKU e a PRIMEIRA PALAVRA DO TITULO DO ATON estiver no TITULO para marketplace em qualquer posição.\n\
MUITO ALTA: Caso o CODID NÃO estiver presente no SKU e a PRIMEIRA PALAVRA DO TITULO DO ATON NÃO estiver no TITULO para marketplace em qualquer posição.\n\
VAZIO: Produto não tem descrição.\n')