import pandas as pd
import pyperclip
from mordomo.main import *
from mordomo.auxiliar import *
from mordomo.login import *

dados = pd.read_excel('excel/trocar_descricao.xlsx')

matar_ambar()
executa_icone_aton()
login_aton()
menu_produtos()
opcao_cadastro_produtos()
cadastro_produtos_botao_consultar()
consultar_produtos_opcao_todos()
consultar_produtos_menu_cod_id()
tamanho_planinha = len(dados)

# FOR
for i in range(tamanho_planinha):
    print(str(i) + '/' + str(tamanho_planinha))
    consultar_produtos_pesquisa()
    pyperclip.copy(dados['cod_interno'][0])
    pg.hotkey('ctrl', 'v')
    consultar_produtos_botao_consultar()
    consultar_produtos_select_resultado()
    cadastro_produtos_botao_alterar()
    cadastro_produtos_descricao()
    pg.press('up', presses=100)
    pg.press('end')
    pg.moveTo(487, 658)
    pg.mouseDown()
    pg.moveTo(1217, 657)
    pg.mouseUp()
    pg.press('backspace')
    pyperclip.copy(dados['titulo'][0])
    pg.hotkey('ctrl', 'v')
    cadastro_produtos_botao_salvar()
    cadastro_produtos_botao_consultar()
