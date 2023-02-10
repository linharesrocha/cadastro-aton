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

# Pega todos os produtos que deram erro 'ID Variação não vinculado ao Produto Pai .'
comando = f'''
SELECT AUTOID, AUTOIDPAI, STATUSCODE, RETORNOSTR, SKURETORNO, FLAG, ERRO_API
FROM PUBLICA_PRODUTO
WHERE DATATH > '08-02-2023'
AND ERRO_API LIKE 'ID Vari%'
'''

df_erros_id_variacao = pd.read_sql(comando, conexao)

# Transformando a coluna AUTOIDPAI em um Set e removendo o AUTOIDPAI 0
autoidpai_set = set(df_erros_id_variacao['AUTOIDPAI'])
autoidpai_set.discard(0)
print(Fore.LIGHTBLUE_EX, f'\nQuantidades de AUTOIDPAI: {str(len(autoidpai_set))}')

for autoidpai in autoidpai_set:
    # Altera de erro para publicação
    comando = f'''
    UPDATE PUBLICA_PRODUTO
    SET FLAG = '0'
    WHERE DATATH > '08-02-2023'
    AND ERRO_API LIKE 'ID Vari%'
    AND AUTOIDPAI = '{autoidpai}'
    '''
    
    cursor.execute(comando)
    conexao.commit()
    
    # Aguarda um segundo antes de consultar
    sleep(1)
    
    # Botão Consultar
    pg.moveTo(771, 84)
    pg.click()
    sleep(1)
    
    # Botão Publicar anúncios
    pg.moveTo(1840, 1014)
    pg.click()
    sleep(0.5)

    # Confirmar publicação
    pg.press('enter')
    sleep(0.5)
    
    # Enter Publicar anúncio
    pg.press('enter')
    sleep(0.5)
    
    # Confirma publicação
    pg.press('left')
    pg.press('enter')

    # Botão Publicar anúncios
    pg.moveTo(1840, 1014)
    pg.click()
    sleep(0.5)


    
    
    # Botão Consultar
    pg.moveTo(771, 84)
    pg.click()
    sleep(0.5)
    
    # Contagem de 20 segundos para publicação
    print(Fore.LIGHTBLUE_EX, f'\nAUTOIDPAI: {autoidpai}')
    for i in range(20):
        if i < 9:
            print(Fore.GREEN, i + 1)
            sleep(1)
        elif i < 15:
            print(Fore.LIGHTYELLOW_EX, i + 1)
            sleep(1)
        else:
            print(Fore.RED, i + 1)
            sleep(1)
            
    print(Fore.LIGHTBLUE_EX,'-' * 50)
    
    # 

    
