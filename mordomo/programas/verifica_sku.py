from mordomo.auxiliar import *
import pyperclip
import pandas as pd

dados = pd.read_excel('excel/Pasta1.xlsx')
print(dados)

tamanho_planilha = len(dados)
for index_produto in range(0, tamanho_planilha):
    print(str(index_produto) + '/' + str(tamanho_planilha) + ' -- ' + dados['cod_interno'][index_produto])
    consultar_produtos_pesquisa()
    pyperclip.copy(dados['cod_interno'][index_produto])
    pg.hotkey('ctrl', 'v')
    consultar_produtos_botao_consultar()
    sleep(2)
    consultar_produtos_select_resultado()
    cadastro_produtos_aba_ficha_tecnica()
    pg.moveTo(530, 412)
    pg.rightClick()
    pg.moveTo(590, 415)
    pg.click()
    pg.moveTo(648, 335)
    pg.click()
    pg.typewrite('C')
    input('Continue')
    pg.moveTo(1145, 751)
    pg.click()
    cadastro_produtos_aba_cadastro_produtos()
    cadastro_produtos_botao_consultar()