import numpy
import slack
from datetime import date, timedelta
from mordomo.auxiliar import *
from mordomo.main import *
import pandas as pd
import time



# Data
today = date.today()
old_d1 = today - timedelta(1)

old_d1 = old_d1.strftime("%d-%m-%Y")
d1 = today.strftime("%d-%m-%Y")


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

matar_slack()
matar_ambar()
executa_icone_aton()
login_aton()
entrar_na_tela_f8()
f8_limpa_empresas()
f8_checkbox_faturados()
f8_data_pre()
pg.hotkey('ctrl', 'a')
pg.press('backspace')
pg.typewrite(old_d1)
f8_menu_etiquetas()
f8_menu_etiquetas_opcao_pendentes_impressao()


app.chat_postMessage(channel='pedidos-diarios', text=' ')
app.chat_postMessage(channel='pedidos-diarios', text='======================================')
for i in range(5):
    app.chat_postMessage(channel='pedidos-diarios', text=d1)

app.chat_postMessage(channel='pedidos-diarios', text='======================================')
app.chat_postMessage(channel='pedidos-diarios', text=' ')

aux = 1
for marketplace in lista_marketplaces:
    f8_menu_origem()
    pg.typewrite(marketplace)

    f8_botao_consultar()
    f8_gerar_relatorio_excel()
    sleep(1)
    pg.press('enter')

    dados = pd.read_excel('C:/Ambar/Docs/RelPedidosCor.xls')

    quantidade_pedidos = dados['Número'].iloc[-1]
    total_pedidos = dados['Total Pedido'].iloc[-1]

    check = pd.isna(total_pedidos)
    if check == True:
        total_pedidos = 0
    total_pedidos = round(total_pedidos, 2)

    # lista
    lista_quantidade_total.append(quantidade_pedidos)
    lista_valores_total.append(total_pedidos)


    # SLACK
    app.chat_postMessage(channel='pedidos-diarios', text=marketplace)
    app.chat_postMessage(channel='pedidos-diarios', text='Quantidade Pedidos = ' + str(quantidade_pedidos))
    app.chat_postMessage(channel='pedidos-diarios', text='Valor Total Pedido = ' + 'R$' + str(total_pedidos))
    app.chat_postMessage(channel='pedidos-diarios', text=' ')


# Somar Valores
app.chat_postMessage(channel='pedidos-diarios', text=' ')
app.chat_postMessage(channel='pedidos-diarios', text='======================================')
app.chat_postMessage(channel='pedidos-diarios', text='Quantidade de Pedidos Total: ' + str(sum(lista_quantidade_total)))
app.chat_postMessage(channel='pedidos-diarios', text='Quantidade de Valor Total: R$' + str(round(sum(lista_valores_total),2)))
app.chat_postMessage(channel='pedidos-diarios', text='======================================')