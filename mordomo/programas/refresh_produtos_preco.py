import pyperclip
from mordomo.main import *
from mordomo.auxiliar import *
import pandas as pd

dados = pd.read_excel('excel/confere_descricao.xls')
pd.set_option('mode.chained_assignment', None)

tamanho_planinha = len(dados)

for i in range(tamanho_planinha):
    print(str(i) + '/' + str(tamanho_planinha) + ' -- ' + dados['Descrição'][i])
    print(' ')
    consultar_produtos_pesquisa()
    pyperclip.copy(dados['Código Interno'][i])
    pg.hotkey('ctrl', 'v')
    consultar_produtos_botao_consultar()
    consultar_produtos_select_resultado()
    cadastro_produtos_botao_skus()
    cadastro_produtos_skus_botao_refresh()
    # close aba
    pg.moveTo(1476, 173)
    pg.click()
    cadastro_produtos_botao_consultar()
