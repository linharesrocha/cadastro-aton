import pyperclip
from mordomo.main import *
from mordomo.auxiliar import *
import pandas as pd

dados = pd.read_excel('excel/atributos_ml.xls')

tamanho_planilha = len(dados)
for index_produto in range(0, tamanho_planilha):
    print(str(index_produto) + '/' + str(tamanho_planilha) + ' -- ' + dados['descricao'][index_produto])
    consultar_produtos_pesquisa()
    pyperclip.copy(dados['descricao'][index_produto])
    pg.hotkey('ctrl', 'v')
    consultar_produtos_botao_consultar()
    sleep(2)
    consultar_produtos_select_resultado()
    cadastro_produtos_aba_ficha_tecnica()
    cadastro_produtos_ficha_tecnica_menu_mercadolivre()

    pg.moveTo(534, 414)
    pg.rightClick()
    sleep(0.2)
    pg.moveTo(568, 427)
    pg.click()
    sleep(0.2)
    pg.moveTo(648, 317)
    pg.click()
    sleep(0.2)
    teste = input('Registrar Marca? (S): ')
    teste = teste.upper()
    for i in range(10):
        print(' ')

    if teste == 'S':
        pg.moveTo(694, 335)
        pg.click()
        sleep(0.2)
        pg.moveTo(1016, 337)
        pg.doubleClick()
        sleep(0.2)
        pg.moveTo(1142, 744)
        pg.click()
        sleep(0.2)
        pg.moveTo(1274, 280)
        pg.click()
        sleep(0.2)
        pyperclip.copy(dados['marca'][index_produto])
        pg.hotkey('ctrl', 'v')

        stop = input('SKU? (S): ')
        stop = stop.upper()
        if stop == 'S':
            cadastro_produtos_aba_cadastro_produtos()
            cadastro_produtos_botao_alterar()
            cadastro_produtos_codigo_interno()
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            cod_interno = pyperclip.paste()
            print(cod_interno)
            cadastro_produtos_botao_cancelar()
            cadastro_produtos_aba_ficha_tecnica()
            pg.moveTo(551, 414)
            pg.click()
            pg.rightClick()
            pg.moveTo(575, 431)
            pg.click()
            pg.moveTo(648, 337)
            pg.click()
            input('Esperando colocar o SKU.')

        cadastro_produtos_ficha_tecnica_botao_salvar()
        cadastro_produtos_aba_cadastro_produtos()
        cadastro_produtos_botao_consultar()
    else:
        pg.moveTo(1235, 749)
        pg.click()
        cadastro_produtos_aba_cadastro_produtos()
        cadastro_produtos_botao_consultar()
