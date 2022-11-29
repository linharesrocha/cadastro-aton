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

    # Pega SKU
    cadastro_produtos_botao_alterar()
    cadastro_produtos_codigo_interno()
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    cadastro_produtos_botao_cancelar()
    cadastro_produtos_aba_ficha_tecnica()
    cadastro_produtos_ficha_tecnica_menu_mercadolivre()
    cadastro_produtos_ficha_tecnica_botao_adicionar()

    # ID
    pg.moveTo(944, 281)
    pg.click()
    pg.typewrite('SELLER_SKU')

    # Nome
    pg.moveTo(1074, 277)
    pg.click()
    pg.typewrite('SKU')

    # Valor
    pg.moveTo(1251, 283)
    pg.doubleClick()
    pg.hotkey('ctrl', 'v')

    # Rola barra
    pg.moveTo(1422, 559)
    pg.click()
    pg.click()
    pg.click()

    # Checkbox caixinha Var
    pg.moveTo(1267, 280)
    pg.doubleClick()

    cadastro_produtos_ficha_tecnica_botao_salvar()
    cadastro_produtos_aba_cadastro_produtos()
    cadastro_produtos_botao_consultar()