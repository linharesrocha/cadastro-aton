import os
from pathlib import Path
import pyodbc
import warnings
import slack
import pandas as pd
from dotenv import load_dotenv
from time import sleep

warnings.filterwarnings('ignore')

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

# GET LAST ORDER
comando = f'''
    SELECT PEDIDO
    FROM PEDIDO_MATERIAIS_CLIENTE
    ORDER BY PEDIDO
    '''

data = pd.read_sql(comando, conexao)
ultimo_pedido = int(data['PEDIDO'].iloc[-1])
pedido_id = ultimo_pedido + 1

while True:
    comando = f'''
    SELECT A.PEDIDO, A.EMPRESA, A.VENDEDOR, A.ORIGEM, A.TOTAL_PEDIDO, A.NF_ID,
    B.DESCRICAOPROD, B.DESCRICAOWEB
    FROM PEDIDO_MATERIAIS_CLIENTE A
    LEFT JOIN PEDIDO_MATERIAIS_ITENS_CLIENTE B
    ON A.PEDIDO = B.PEDIDO 
    WHERE A.PEDIDO = '{pedido_id}'
    '''
    data = pd.read_sql(comando, conexao)

    if len(data['PEDIDO']) == 0:
        print(f'Aguardando o pedido {pedido_id}')
        sleep(120)
    else:
        try:
            id_empresa = data['EMPRESA'].item()
        except:
            aux_list = ['EMPRESA'].tolist()
            id_empresa = aux_list[0]
        empresa = ''
        if id_empresa == 1:
            empresa = 'MADZ'
        elif id_empresa == 2:
            empresa = 'LEAL'
        elif id_empresa == 3:
            empresa = 'PISSTE'
        else:
            empresa = 'MADZ FILIAL SP'

        vendedor = str(data['VENDEDOR'].item())
        vendedor = vendedor.replace('  ', '')
        descricaoprod = str(data['DESCRICAOPROD'].item()).replace('   ', '')
        descricaoweb = str(data['DESCRICAOWEB'].item())

        # Confere se ta vazio
        if not descricaoprod:
            nome_produto = descricaoweb
        else:
            nome_produto = descricaoprod

        app.chat_postMessage(channel='pedidos-novos', text="Canal: " + vendedor + ' ' + empresa)
        app.chat_postMessage(channel='pedidos-novos', text="Produto: " + nome_produto)
        app.chat_postMessage(channel='pedidos-novos', text="Total_Pedido: R$" + str(data['TOTAL_PEDIDO'].item()))
        app.chat_postMessage(channel='pedidos-novos', text="NF: " + str(data['NF_ID'].item()))
        app.chat_postMessage(channel='pedidos-novos', text="============================")

        # app.chat_postMessage(channel='tendencias-test', text="Canal: " + vendedor + ' ' + empresa)
        # app.chat_postMessage(channel='tendencias-test', text="Produto: " + nome_produto)
        # app.chat_postMessage(channel='tendencias-test', text="Total_Pedido: R$" + str(data['TOTAL_PEDIDO'].item()))
        # app.chat_postMessage(channel='tendencias-test', text="NF: " + str(data['NF_ID'].item()))
        # app.chat_postMessage(channel='tendencias-test', text="============================")
        pedido_id += 1