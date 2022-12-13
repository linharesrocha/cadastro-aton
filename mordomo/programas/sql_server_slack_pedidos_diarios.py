import warnings
from pathlib import Path
import slack
from datetime import date, timedelta, datetime
from dotenv import load_dotenv
import os
import pandas as pd
import pyodbc

# Data
dia_da_semana = str(datetime.today().strftime('%A'))
remove_dias = 1
if dia_da_semana == 'Monday':
    remove_dias = 3
today = date.today()
old_d1 = today - timedelta(remove_dias)
old_d1 = old_d1.strftime("%d-%m-%Y")
date_today = today + timedelta(1)
d1 = date_today.strftime("%d-%m-%Y")

warnings.filterwarnings('ignore')

lista_marketplaces = [
    'NETSHOES MADZ', 'NETSHOES LEAL', 'NETSHOES PISSTE',
    'DAFITI MADZ', 'DAFITI LEAL', 'DAFITI PISSTE',
    'ML MADZ', 'ML LEAL', 'ML PISSTE',
    'SHOPEE MADZ', 'SHOPEE LEAL', 'SHOPEE PISSTE',
    'CARREFOUR MADZ', 'CARREFOUR LEAL', 'CARREFOUR PISSTE',
    'B2W MADZ', 'B2W LEAL', 'B2W PISSTE',
    'AMAZON MADZ', 'AMAZON LEAL', 'AMAZON PISSTE',
    'MAGALU MADZ', 'MAGALU LEAL', 'MAGALU PISSTE',
    'VIA VAREJO MADZ', 'TRAY', 'DECATHLON']

lista_quantidade_total = []
lista_valores_total = []


# SLACK SETUP
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
app = slack.WebClient(token=os.environ['SLACK_TOKEN'])
env_path_sql = Path('.') / '.env-sql'
load_dotenv(dotenv_path=env_path_sql)
DATABASE=os.environ['DATABASE']
UID=os.environ['UID']
PWD=os.environ['PWD']

dados_conexao = ("Driver={SQL Server};"
            "Server=erp.ambarxcall.com.br;"
            "Database="+DATABASE+";"
            "UID="+UID+";"
            "PWD="+PWD+";")

conexao = pyodbc.connect(dados_conexao)
print("Conexão com o Banco de Dados Bem Sucedida!")
cursor = conexao.cursor()


comando = f'''
    SELECT *
    FROM PEDIDO_MATERIAIS_CLIENTE
    WHERE DATA BETWEEN '12-12-2022' AND '14-12-2022'
    AND POSICAO = 'EMITIDO'
    '''

data = pd.read_sql(comando, conexao)

# Coletando quantidade de pedidos no dia e valor total
quantidade_pedidos = data.shape[0]
total_pedidos = round(data['TOTAL_PEDIDO'].sum(), 2)

# app.chat_postMessage(channel='tendencias-test', text=' ')
# app.chat_postMessage(channel='tendencias-test', text='======================================')
# for i in range(5):
#     app.chat_postMessage(channel='tendencias-test', text=d1)
#
# app.chat_postMessage(channel='tendencias-test', text='======================================')
# app.chat_postMessage(channel='tendencias-test', text=' ')

aux = 1
for marketplace in lista_marketplaces:
    break

    # SLACK
    app.chat_postMessage(channel='tendencias-test', text=marketplace)
    app.chat_postMessage(channel='tendencias-test', text='Quantidade Pedidos = ' + str(quantidade_pedidos))
    app.chat_postMessage(channel='tendencias-test', text='Valor Total Pedido = ' + 'R$' + str(total_pedidos))
    app.chat_postMessage(channel='tendencias-test', text=' ')


# Somar Valores
# app.chat_postMessage(channel='tendencias-test', text=' ')
# app.chat_postMessage(channel='tendencias-test', text='======================================')
# app.chat_postMessage(channel='tendencias-test', text='Quantidade de Pedidos Total: ' + str(sum(lista_quantidade_total)))
# app.chat_postMessage(channel='tendencias-test', text='Quantidade de Valor Total: R$' + str(round(sum(lista_valores_total),2)))
# app.chat_postMessage(channel='tendencias-test', text='======================================')