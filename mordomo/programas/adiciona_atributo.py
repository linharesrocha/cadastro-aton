import pyperclip
from mordomo.main import *
from mordomo.auxiliar import *
import pandas as pd

dados = pd.read_excel('excel/atributos.xlsx')

listaFeitos = []
listaNaoFeitos = []

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
    cadastro_produtos_ficha_tecnica_menu_netshoes()

    # Clica no valor
    pg.moveTo(702, 280)
    pg.click()
    sleep(1.5)

    # Copia valor
    pg.hotkey('ctrl', 'c')
    teste = pyperclip.paste()

    if teste == 'Nome	Valor	Var	Allow':
        listaFeitos.append(dados['descricao'][index_produto])
        # Marcas
        cadastro_produtos_ficha_tecnica_botao_adicionar()
        cadastro_produtos_ficha_tecnica_campo_nome()
        pg.typewrite('Marcas')
        cadastro_produtos_ficha_tecnica_campo_valor()
        pyperclip.copy(dados['marca'][index_produto])
        pg.hotkey('ctrl', 'v')

        # Cores
        cadastro_produtos_ficha_tecnica_botao_adicionar()
        cadastro_produtos_ficha_tecnica_campo_nome()
        pg.typewrite('Cores')
        cadastro_produtos_ficha_tecnica_campo_valor()
        pyperclip.copy(dados['cor'][index_produto])
        pg.hotkey('ctrl', 'v')

        # Tamanhos
        cadastro_produtos_ficha_tecnica_botao_adicionar()
        cadastro_produtos_ficha_tecnica_campo_nome()
        pg.typewrite('Tamanhos')
        cadastro_produtos_ficha_tecnica_campo_valor()
        pyperclip.copy(dados['tamanho'][index_produto])
        pg.hotkey('ctrl', 'v')

        # Gênero
        cadastro_produtos_ficha_tecnica_botao_adicionar()
        cadastro_produtos_ficha_tecnica_campo_nome()
        pyperclip.copy('Gênero')
        pg.hotkey('ctrl', 'v')
        cadastro_produtos_ficha_tecnica_campo_valor()
        pyperclip.copy(dados['genero'][index_produto])
        pg.hotkey('ctrl', 'v')

        # Departamento BS
        cadastro_produtos_ficha_tecnica_botao_adicionar()
        cadastro_produtos_ficha_tecnica_campo_nome()
        pg.typewrite('Departamento BS')
        cadastro_produtos_ficha_tecnica_campo_valor()
        pyperclip.copy(dados['departamento_bs'][index_produto])
        pg.hotkey('ctrl', 'v')
    else:
        listaNaoFeitos.append(dados['descricao'][index_produto])

    cadastro_produtos_ficha_tecnica_botao_salvar()
    cadastro_produtos_aba_cadastro_produtos()
    cadastro_produtos_botao_consultar()

print('feitos')
print(len(listaFeitos))

print('nao feitos')
print(listaNaoFeitos)