import pyperclip
from mordomo.auxiliar import *
import pandas as pd

dados = pd.read_excel('excel/b2w_madz.xlsx')
cod_id_lista = dados['cod_id'].tolist()
nomes_lista = dados['titulo'].tolist()
preco_de_lista = dados['preco_de'].tolist()
preco_de_lista = list(map(str, preco_de_lista))

preco_por_lista = dados['preco_por'].tolist()
preco_por_lista = list(map(str, preco_por_lista))

tamanho_dados = len(dados)

for id in cod_id_lista:
    # ID
    pg.moveTo(76, 87)
    pg.click()
    pg.hotkey('ctrl', 'a')
    pg.press('backspace')
    pyperclip.copy(id)
    pg.hotkey('ctrl', 'v')

    # Procurando o Index do Id
    index = dados[dados['cod_id'] == id].index.values
    index = index[0]

    # Botao consultar
    pg.moveTo(774, 81)
    pg.click()
    sleep(1)

    # Preenche nome
    pg.moveTo(825, 165)
    pg.click()
    pyperclip.copy(nomes_lista[index])
    pg.hotkey('ctrl', 'v')

    # Preenchendo Preço De
    pg.moveTo(1510, 165)
    pg.click()
    pyperclip.copy(preco_de_lista[index].replace('.', ','))
    pg.hotkey('ctrl', 'v')

    # Preenche Preço Por
    pg.moveTo(1610, 165)
    pg.click()
    pyperclip.copy(preco_por_lista[index].replace('.', ','))
    pg.hotkey('ctrl', 'v')
    pg.press('up')
