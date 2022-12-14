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
    'NETSHOES',
    'DAFITI',
    'MERCADO LIVRE',
    'SHOPEE',
    'CARREFOUR',
    'LOJASAMERICANAS',
    'AMAZON',
    'MAGAZINE LUIZA',
    'VIA VAREJO',
    'TRAY',
    'DECATHLON',
    'SHOPTIME',
    'OLIST',
    'SUBMARINO']

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
cursor = conexao.cursor()
print("Conexão com o Banco de Dados Bem Sucedida!")


comando = f'''
    SELECT PEDIDO, EMPRESA, DATA, ORIGEM, VENDEDOR, TOTAL_PEDIDO
    FROM PEDIDO_MATERIAIS_CLIENTE
    WHERE DATA BETWEEN '{old_d1}' AND '{d1}'
    AND POSICAO = 'EMITIDO'
    '''

data = pd.read_sql(comando, conexao)

# Coletando quantidade de pedidos no dia e valor total
quantidade_pedidos_total = data.shape[0]
pedidos_total = round(data['TOTAL_PEDIDO'].sum(), 2)

# app.chat_postMessage(channel='tendencias-test', text=' ')
# app.chat_postMessage(channel='tendencias-test', text='======================================')
# for i in range(5):
#     app.chat_postMessage(channel='tendencias-test', text=d1)
#
# app.chat_postMessage(channel='tendencias-test', text='======================================')
# app.chat_postMessage(channel='tendencias-test', text=' ')


for marketplace in lista_marketplaces:
    data_marketplace = data[data['VENDEDOR'].str.contains(marketplace, na=False)]
    data_marketplace_madz = data_marketplace.loc[data_marketplace['EMPRESA'] == 1]
    data_marketplace_leal =  data_marketplace.loc[data_marketplace['EMPRESA'] == 2]
    data_marketplace_pisste = data_marketplace.loc[data_marketplace['EMPRESA'] == 3]

    # MADZ
    quantidade_pedidos_total_mktp_madz = data_marketplace_madz.shape[0]
    pedidos_total_mktp_madz = round(data_marketplace_madz['TOTAL_PEDIDO'].sum(), 2)

    # LEAL
    quantidade_pedidos_total_mktp_leal = data_marketplace_leal.shape[0]
    pedidos_total_mktp_leal = round(data_marketplace_leal['TOTAL_PEDIDO'].sum(), 2)

    # PISSTE
    quantidade_pedidos_total_mktp_pisste = data_marketplace_pisste.shape[0]
    pedidos_total_mktp_pisste = round(data_marketplace_pisste['TOTAL_PEDIDO'].sum(), 2)


    # SLACK
    str_1 = f"{marketplace} MADZ" \
            f"\nQuantidade Pedidos = {str(quantidade_pedidos_total_mktp_madz)}" \
            f"\nValor Total Pedido = R${str(pedidos_total_mktp_madz)}" \
            f"\n. " \
            f"\n" \
            f"{marketplace} LEAL" \
            f"\nQuantidade Pedidos = {str(quantidade_pedidos_total_mktp_leal)}" \
            f"\nValor Total Pedido = R${str(pedidos_total_mktp_leal)}" \
            f"\n. " \
            f"\n" \
            f"{marketplace} PISSTE" \
            f"\nQuantidade Pedidos = {str(quantidade_pedidos_total_mktp_pisste)}" \
            f"\nValor Total Pedido = R${str(pedidos_total_mktp_pisste)}" \
            f"\n." \
            f"\n" \

    app.chat_postMessage(channel='tendencias-test', text=str_1)
    break


# # Somar Valores
# app.chat_postMessage(channel='tendencias-test', text=' ')
# app.chat_postMessage(channel='tendencias-test', text='======================================')
# app.chat_postMessage(channel='tendencias-test', text='Quantidade de Pedidos Total: ' + str(quantidade_pedidos_total))
# app.chat_postMessage(channel='tendencias-test', text='Quantidade de Valor Total: R$' + str(pedidos_total_mktp))
# app.chat_postMessage(channel='tendencias-test', text='======================================')