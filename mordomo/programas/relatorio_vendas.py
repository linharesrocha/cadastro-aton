import slack

from mordomo.auxiliar import *
from mordomo.main import *
import pandas as pd
import time
from datetime import date

# Start time
st = time.time()

# Formating Date
today = date.today()
d1 = today.strftime("%d-%m-%Y")

lista_marketplaces = [
    'NETSHOES MADZ', 'NETSHOES LEAL', 'NETSHOES PISSTE']
    # 'DAFITI MADZ', 'DAFITI LEAL', 'DAFITI PISSTE',
    # 'ML MADZ', 'ML LEAL', 'ML PISSTE',
    # 'SHOPEE MADZ', 'SHOPEE LEAL', 'SHOPEE PISSTE',
    # 'CARREFOUR MADZ', 'CARREFOUR LEAL', 'CARREFOUR PISSTE',
    # 'B2W MADZ', 'B2W LEAL', 'B2W PISSTE',
    # 'AMAZON MADZ', 'AMAZON LEAL', 'AMAZON PISSTE',
    # 'MAGALU MADZ', 'MAGALU LEAL', 'MAGALU PISSTE',
    # 'CENTAURO MADZ', 'CENTAURO LEAL',
    # 'OLIST MADZ', 'VIA VAREJO MADZ', 'TRAY', 'DECATHLON']


# SLACK SETUP
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
app = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# matar_ambar()
# executa_icone_aton()
# login_aton()
# menu_vendas()
# vendas_relatorios_gerenciais()
# vendas_relatorios_vendas_pedidos()
# relatorio_analise_venda_checkbox_abertos()

app.chat_postMessage(channel='tendencias-test', text=d1)

for marketplace in lista_marketplaces:
    relatorio_analise_venda_menu_origem()
    pg.typewrite(marketplace)

    relatorio_analise_venda_botao_consultar()
    relatorio_analise_venda_gerar_relatorio()
    pg.press('enter')

    dados = pd.read_excel('C:/Ambar/Docs/RelVendasEcom01.xls')

    quantidade_pedidos = str(dados['PEDIDO'].iloc[-1])
    total_custo = str(dados['TOTAL CUSTO'].iloc[-1])
    total_pedidos = str(dados['TOTAL PEDIDO'].iloc[-1])

    # SLACK
    app.chat_postMessage(channel='tendencias-test', text=marketplace)
    app.chat_postMessage(channel='tendencias-test', text='Quantidade Pedidos = ' + quantidade_pedidos)
    app.chat_postMessage(channel='tendencias-test', text='Total Custo = ' + total_custo)
    app.chat_postMessage(channel='tendencias-test', text='Total Pedidos = ' + total_pedidos)
    app.chat_postMessage(channel='tendencias-test', text=' ')