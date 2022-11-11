import pandas as pd
import pyperclip

from mordomo.auxiliar import *


dados = pd.read_excel('excel/skyhub_vinculacao.xlsx')
quantidade_produtos = len(dados)
sku_lista = dados['SKU'].tolist()

aux = 0
# Deixe na pagina inicial de produtos --> https://in.skyhub.com.br/products#/
for sku in sku_lista:
    print(str(aux + 1) + '/' + str(quantidade_produtos) + ' --> ' + sku)
    pg.moveTo(683, 456)
    pg.click()
    pyperclip.copy(sku_lista[aux])
    pg.hotkey('ctrl', 'v')

    # Filtro
    pg.moveTo(1851, 333)
    pg.click()
    sleep(2)

    # Seleciona produto
    pg.moveTo(226, 543)
    sleep(1)
    pg.click()

    # Seleciona plataforma Menu
    pg.moveTo(1424, 230)
    pg.click()

    # Seleciona B2W
    pg.moveTo(1433, 292)
    pg.click()

    # Menu Ações
    pg.moveTo(1698, 231)
    pg.click()

    # Seleciona conectar
    pg.moveTo(1669, 292)
    pg.click()

    # Clica em executar
    pg.moveTo(1844, 233)
    pg.click()
    sleep(1)
    pg.press('enter')
    sleep(3)
    pg.press('enter')


    # Menu Produtos
    pg.moveTo(62, 278)
    pg.click()

    # Gerenciar produtos
    pg.moveTo(90, 318)
    pg.click()
    sleep(3)
    aux = aux + 1