from mordomo.main import *
from mordomo.auxiliar import *
import pandas as pd

dados = pd.read_excel('excel/INATIVAR_PRODUTOS.xls')

for i in range(len(dados)):
    print(str(i) + '/' + str(len(dados)) + ' -- ' + dados['codigo'][i])
    consultar_produtos_pesquisa()
    pyperclip.copy(dados['codigo'][i])
    pg.hotkey('ctrl', 'v')
    consultar_produtos_botao_consultar()
    consultar_produtos_select_resultado()
    cadastro_produtos_botao_alterar()
    pg.moveTo(1311, 290)
    pg.click()
    cadastro_produtos_botao_salvar()
    cadastro_produtos_botao_consultar()