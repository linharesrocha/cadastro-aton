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

dados_conexao = ("Driver={SQL Server};"
                 "Server=erp.ambarxcall.com.br;"
                 "Database=" + DATABASE + ";"
                                          "UID=" + UID + ";"
                                                         "PWD=" + PWD + ";")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()
comando = '''
SELECT CODID, COD_INTERNO, DESCRICAO, DESCRITIVO
FROM MATERIAIS
WHERE INATIVO = 'N'
AND DESCRITIVO IS NOT NULL
AND PAI = '0'
'''

data = pd.read_sql(comando, conexao)
descritivo_lista = data['DESCRITIVO'].tolist()
primeiro_nome = []
primeiro_nome_60_caract = []
primeiro_nome_diferenca = []

# Derivando titulo da descricao
for descritivo in descritivo_lista:
    aux = 0
    titulo_descricao = descritivo.splitlines()[0]
    titulo_descricao = titulo_descricao.title()
    primeiro_nome.append(titulo_descricao)
data['PRIMEIRO_NOME'] = primeiro_nome

for titulo in primeiro_nome:
    string_final_list = []
    count = 0
    aux = 0
    if len(titulo) > 60:
        string_list = titulo.split(' ')
        for string in string_list:
            count = count + len(string) + 1
            if count <= 60:
                string_final_list.append(string)
            else:
                count = count - 1
                if count <= 60:
                    string_final_list.append(string)
                else:
                    break

        string_final = ' '.join(string_final_list)
        if len(string_final) > 60:
            string_final_list = string_final.split(' ')
            string_final_list.pop()
            string_final = ' '.join(string_final_list)
    primeiro_nome_60_caract.append(string_final)
data['PRIMEIRO_NOME_60'] = primeiro_nome_60_caract

# See difference between two lists
for i in range(len(primeiro_nome_60_caract)):
    aux1 = primeiro_nome_60_caract[i]
    aux2 = primeiro_nome[i]
    list_aux1 = aux1.split(' ')
    list_aux2 = aux2.split(' ')
    set_aux1 = set(list_aux1)
    set_aux2 = set(list_aux2)

    result_difference = list(set_aux2 - set_aux1)
    name_difference = ' '.join(result_difference)
    primeiro_nome_diferenca.append(name_difference)

data['DIFERENCA'] = primeiro_nome_diferenca
data.to_excel('excel/primeiro_nome_com_60.xls', index=False)
