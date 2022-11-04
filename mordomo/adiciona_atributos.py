from main import *
from auxiliar import *
from setup import *
import pandas as pd

dados = pd.read_excel('cores.xlsx')

matar_ambar()
executa_icone_aton()
login_aton()
menu_produtos()
opcao_cadastro_produtos()
cadastro_produtos_botao_consultar()
consultar_produtos_opcao_todos()

tamanho_planilha = len(dados)
for index_produto in range(0, tamanho_planilha):
    print(str(index_produto) + '/' + str(tamanho_planilha) + ' -- ' + dados['descricao'][index_produto])
    consultar_produtos_pesquisa()
    pyperclip.copy(dados['descricao'][index_produto])
    pg.hotkey('ctrl', 'v')
    consultar_produtos_botao_consultar()
    consultar_produtos_select_resultado()
    cadastro_produtos_aba_ficha_tecnica()

    cadastro_produtos_ficha_tecnica_menu_magalu()
    cadastro_produtos_ficha_tecnica_botao_adicionar()
    cadastro_produtos_ficha_tecnica_campo_nome()
    pg.typewrite('Cores')
    cadastro_produtos_ficha_tecnica_campo_valor()
    pyperclip.copy(dados['cor'][index_produto])
    pg.hotkey('ctrl', 'v')
    cadastro_produtos_ficha_tecnica_botao_salvar()

    cadastro_produtos_ficha_tecnica_menu_skyhub()
    cadastro_produtos_ficha_tecnica_botao_adicionar()
    cadastro_produtos_ficha_tecnica_campo_nome()
    pg.typewrite('Cores')
    cadastro_produtos_ficha_tecnica_campo_valor()
    pyperclip.copy(dados['cor'][index_produto])
    pg.hotkey('ctrl', 'v')
    cadastro_produtos_ficha_tecnica_botao_salvar()

    cadastro_produtos_aba_cadastro_produtos()
    cadastro_produtos_botao_consultar()