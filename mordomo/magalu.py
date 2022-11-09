from main import *
from auxiliar import *
from mordomo.setup import *
import pandas as pd

matar_ambar()
executa_icone_aton()
login_aton()
menu_integracao()
opcao_publicar_anuncio()
publicar_anuncio_filtro_verde()
publicar_anuncio_seleciona_seta_grupo()
publicar_anuncio_seleciona_leal_grupo()
publicar_anuncio_seleciona_marketplace_magalu_leal()
publicar_anuncio_estoque_positivo()
publicar_anuncio_botao_consultar()
publicar_anuncio_clica_filtro_existe()
publicar_anuncio_aba_produtos_selecionados()
publicar_anuncio_aba_produtos_selecionados_asterisco()
publicar_anuncio_aba_produtos_selecionados_asterisco_auto_id()
publicar_anuncio_produtos_selecionado_remove_filtros_ruins()
publicar_anuncio_aba_produtos_selecionados_filtro_auto_id()

stop = 1
while stop < 72:
    publicar_anuncio_aba_consulta_produtos()
    publicar_anuncio_aba_produtos_sobe_barra()
    publicar_anuncio_seleciona_resultado_botao_direito()
    publicar_anuncio_seleciona_resultado_produto()
    cadastro_produtos_botao_alterar()
    cadastro_produtos_valor_custo()

    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    valor_custo = pyperclip.paste()
    valor_custo = valor_custo.replace(',', '.')
    print(valor_custo)
    if valor_custo != '0':
        # Markup
        valor_custo = float(valor_custo)
        valor_custo = valor_custo * 3

        # Convertendo o preço em uma lista de string
        valor_custo_string = str(valor_custo)
        digitos_lista = [*valor_custo_string]
        index_ponto = digitos_lista.index('.')
        valor_alterar_pre = index_ponto - 1
        valor_alterar_pos = index_ponto + 1

        # Pegando o segundo digito
        if digitos_lista[valor_alterar_pre] == '0' or digitos_lista[valor_alterar_pre] == '5' or digitos_lista[
            valor_alterar_pre] == '6' or digitos_lista[valor_alterar_pre] == '7' or digitos_lista[
            valor_alterar_pre] == '8' or digitos_lista[valor_alterar_pre] == '9':
            digitos_lista[valor_alterar_pre] = '9'

        if digitos_lista[valor_alterar_pre] == '1' or digitos_lista[valor_alterar_pre] == '2' or digitos_lista[
            valor_alterar_pre] == '3' or digitos_lista[valor_alterar_pre] == '4':
            digitos_lista[valor_alterar_pre] = '4'

        # Alterando o 128.'9'
        digitos_lista[valor_alterar_pos] = '9'

        valor_custo_final = ''.join(digitos_lista)
        valor_custo_final = float(valor_custo_final)
        porcentagem = (valor_custo_final * 30) / 100
        valor_custo_pre = valor_custo_final + porcentagem
        print(valor_custo_pre)
        print(valor_custo_final)

        # Float To String
        valor_custo_final = str(valor_custo_final).replace('.', ',')
        valor_custo_pre = str(valor_custo_pre).replace('.', ',')
        print(valor_custo_pre)
        print(valor_custo_final)

    else:
        valor_custo_pre = '0'
        valor_custo_final = '0'

    # Pegando nome do produto na descricao
    cadastro_produtos_descricao()
    pg.press('up', presses=100)
    pg.press('end')

    pg.moveTo(487, 658)
    pg.mouseDown()
    pg.moveTo(1217, 657)
    pg.mouseUp()

    pg.hotkey('ctrl', 'c')

    titulo_produto = pyperclip.paste()
    titulo_produto = titulo_produto.strip('"')
    if titulo_produto.isupper():
        titulo_produto = titulo_produto.title()

    cadastro_produtos_fechar()
    publicar_anuncio_seleciona_resultado_botao_direito()
    publicar_anuncio_seleciona_resultado_f2()
    publicar_anuncio_aba_produtos_selecionados()
    publicar_anuncio_produtos_selecionado_sobe_barra()

    FIX_MOVE = 22
    START = 187
    qntd_variacoes = 1

    # Pegando o primeiro para armazenar o original
    pg.moveTo(825, 165)
    pg.click()
    pg.hotkey('ctrl', 'c')
    nome_completo_original = pyperclip.paste()
    primeiro_nome_original = nome_completo_original.split()[0]

    # Verificando quantas variações tem
    verification = 1
    while verification == 1:
        pg.moveTo(825, START)
        pg.click()
        pg.hotkey('ctrl', 'c')
        nome_completo_teste = pyperclip.paste()
        primeiro_nome_teste = nome_completo_teste.split()[0]
        print(primeiro_nome_teste)

        if primeiro_nome_teste == primeiro_nome_original:
            if primeiro_nome_teste.isupper():
                qntd_variacoes = qntd_variacoes + 1
                START = START + 22
                verification = 1
            else:
                verification = 0
        else:
            verification = 0

    # Preenche Nome
    START_NOME = 187
    pg.moveTo(825, 165)
    pg.click()
    pyperclip.copy(titulo_produto)
    for i in range(qntd_variacoes):
        pg.hotkey('ctrl', 'v')
        pg.moveTo(825, START_NOME)
        pg.click()
        START_NOME = START_NOME + 22

    # Prenche Preço De
    START_PRECO_DE = 187
    pg.moveTo(1510, 165)
    pg.click()
    pyperclip.copy(valor_custo_pre)
    for i in range(qntd_variacoes):
        pg.hotkey('ctrl', 'v')
        pg.moveTo(1510, START_PRECO_DE)
        pg.click()
        START_PRECO_DE = START_PRECO_DE + 22

    # Preenche Preço Por
    START_PRECO_POR = 187
    pg.moveTo(1610, 165)
    pg.click()
    pyperclip.copy(valor_custo_final)
    for i in range(qntd_variacoes):
        pg.hotkey('ctrl', 'v')
        pg.moveTo(1610, START_PRECO_POR)
        pg.click()
        START_PRECO_POR = START_PRECO_POR + 22

    stop = stop + 1
    print(stop)
