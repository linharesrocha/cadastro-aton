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
lista_quantidade_total_cnpj_madz = []
lista_quantidade_total_cnpj_leal = []
lista_quantidade_total_cnpj_pisste = []
lista_valores_total_cnpj_madz = []
lista_valores_total_cnpj_leal = []
lista_valores_total_cnpj_pisste = []

# SLACK SETUP
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
app = slack.WebClient(token=os.environ['SLACK_TOKEN'])
env_path_sql = Path('.') / '.env-sql'
load_dotenv(dotenv_path=env_path_sql)
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
print("Conexão com o Banco de Dados Bem Sucedida!")

comando = f'''
    SELECT PEDIDO, EMPRESA, DATA, ORIGEM, VENDEDOR, TOTAL_PEDIDO
    FROM PEDIDO_MATERIAIS_CLIENTE
    WHERE DATA BETWEEN '{old_d1}' AND '{d1}'
    AND POSICAO = 'EMITIDO'
    AND POSICAO_ETQ = '1'
    '''

data = pd.read_sql(comando, conexao)

# Coletando quantidade de pedidos no dia e valor total
quantidade_pedidos_total = data.shape[0]
pedidos_total = round(data['TOTAL_PEDIDO'].sum(), 2)


str_start = f"\n======================================" \
            f"\n{d1}" \
            f"\n{d1}" \
            f"\n{d1}" \
            f"\n{d1}" \
            f"\n======================================"
app.chat_postMessage(channel='tendencias-test', text=str_start)

for marketplace in lista_marketplaces:
    data_marketplace = data[data['VENDEDOR'].str.contains(marketplace, na=False)]
    data_marketplace_madz = data_marketplace.loc[data_marketplace['EMPRESA'] == 1]
    data_marketplace_leal = data_marketplace.loc[data_marketplace['EMPRESA'] == 2]
    data_marketplace_pisste = data_marketplace.loc[data_marketplace['EMPRESA'] == 3]

    # MADZ
    quantidade_pedidos_total_mktp_madz = data_marketplace_madz.shape[0]
    pedidos_total_mktp_madz = round(data_marketplace_madz['TOTAL_PEDIDO'].sum(), 2)
    lista_quantidade_total_cnpj_madz.append(quantidade_pedidos_total_mktp_madz)
    lista_valores_total_cnpj_madz.append(pedidos_total_mktp_madz)

    # LEAL
    quantidade_pedidos_total_mktp_leal = data_marketplace_leal.shape[0]
    pedidos_total_mktp_leal = round(data_marketplace_leal['TOTAL_PEDIDO'].sum(), 2)
    lista_quantidade_total_cnpj_leal.append(quantidade_pedidos_total_mktp_leal)
    lista_valores_total_cnpj_leal.append(pedidos_total_mktp_leal)

    # PISSTE
    quantidade_pedidos_total_mktp_pisste = data_marketplace_pisste.shape[0]
    pedidos_total_mktp_pisste = round(data_marketplace_pisste['TOTAL_PEDIDO'].sum(), 2)
    lista_quantidade_total_cnpj_pisste.append(quantidade_pedidos_total_mktp_pisste)
    lista_valores_total_cnpj_pisste.append(pedidos_total_mktp_pisste)

    # SLACK
    if quantidade_pedidos_total_mktp_madz > 0:
        str_1 = f"{marketplace} MADZ" \
                f"\nQntd:  {str(quantidade_pedidos_total_mktp_madz)}" \
                f"\nValor:  R${str(pedidos_total_mktp_madz)}" \
                f"\n. "
        app.chat_postMessage(channel='tendencias-test', text=str_1)

    if quantidade_pedidos_total_mktp_leal > 0:
        str_2 = f"{marketplace} LEAL" \
                f"\nQntd:  {str(quantidade_pedidos_total_mktp_leal)}" \
                f"\nValor:  R${str(pedidos_total_mktp_leal)}" \
                f"\n. "
        app.chat_postMessage(channel='tendencias-test', text=str_2)

    if quantidade_pedidos_total_mktp_pisste > 0:
        str_3 = f"{marketplace} PISSTE" \
                f"\nQntd:  {str(quantidade_pedidos_total_mktp_pisste)}" \
                f"\nValor:  R${str(pedidos_total_mktp_pisste)}" \
                f"\n. "
        app.chat_postMessage(channel='tendencias-test', text=str_3)

# Relatório em cada CNPJ
qntd_pedidos_madz = sum(lista_quantidade_total_cnpj_madz)
qntd_pedidos_leal = sum(lista_quantidade_total_cnpj_leal)
qntd_pedidos_pisste = sum(lista_quantidade_total_cnpj_pisste)
qntd_vendas_madz = round(sum(lista_valores_total_cnpj_madz),2)
qntd_vendas_leal = round(sum(lista_valores_total_cnpj_leal),2)
qntd_vendas_pisste = round(sum(lista_valores_total_cnpj_pisste),2)


str_cnpj = f"======================================" \
           f"\n SOMA:" \
           f"\n." \
           f"\n MADZ:  {qntd_pedidos_madz}" \
           f"\n LEAL:  {qntd_pedidos_leal}" \
           f"\n PISSTE:  {qntd_pedidos_pisste}" \
           f"\n ." \
           f"\n MADZ:  R${qntd_vendas_madz}" \
           f"\n LEAL:  R${qntd_vendas_leal}" \
           f"\n PISSTE:  R${qntd_vendas_pisste}" \

    # Somar Valores Três CNPJ
str_final = f"\n======================================" \
            f"\nQntd Pedidos Totais:  {str(quantidade_pedidos_total)}" \
            f"\nValor Pedidos Totais:  R${str(float(pedidos_total))}" \
            f"\n======================================"

app.chat_postMessage(channel='tendencias-test', text= str_cnpj)
app.chat_postMessage(channel='tendencias-test', text=str_final)
