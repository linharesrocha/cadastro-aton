import os
import urllib
from pathlib import Path
from urllib.request import urlopen

import pyodbc
import pandas as pd
import warnings
import wget
from PIL.Image import *
import shutil
from dotenv import load_dotenv

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
SELECT A.CODID, B.COD_INTERNO, B.DESCRICAO, A.URL
FROM MATERIAIS_IMAGENS A
LEFT JOIN MATERIAIS B
ON A.CODID = B.CODID
WHERE A.CODID > 0
AND B.INATIVO = 'N'
'''

# data = pd.read_sql(comando, conexao)
data = pd.read_excel('rel_photos_com_status_code.xls')

aux = 0
for id in data['CODID']:
    print('ID: ' + str(id))
    print('URL: ' + data['URL'][aux])
    print(str(aux) +'/'+ str(len(data)))
    url = data['URL'][aux]
    try:
        file_name = wget.download(url)
    except:
        file_name = 'image.jpg'
        urllib.request.urlretrieve(url, file_name)

    old_name = r'C:/workspace/cadastro-aton/mordomo/programas/' + file_name
    new_name = r'C:/workspace/cadastro-aton/mordomo/programas/' + str(id) + '-' +  str(aux) + '.jpg'
    os.rename(old_name, new_name)

    src_path = new_name
    dst_path = r"C:/DAGG_IMAGES" + '/' + str(id) + '-' +  str(aux) + '.jpg'
    shutil.move(src_path, dst_path)

    aux = aux + 1