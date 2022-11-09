import pyperclip
from main import *
from auxiliar import *
from mordomo.setup import *

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
while stop < 5:
    publicar_anuncio_aba_consulta_produtos()
    publicar_anuncio_aba_produtos_sobe_barra()
    publicar_anuncio_seleciona_resultado_botao_direito()
    publicar_anuncio_seleciona_resultado_produto()
    cadastro_produtos_botao_alterar()

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

    # Pegando valor de custo
    lista_valores_custo = []
    START_VALOR_CUSTO_Y = 165
    for i in range(qntd_variacoes):
        pg.moveTo(1428, START_VALOR_CUSTO_Y)
        pg.click()
        pg.hotkey('ctrl', 'c')
        cabecalho = pyperclip.paste()
        lista_valores_cabecalho = cabecalho.split("\t")
        valor_custo = lista_valores_cabecalho[-3]
        valor_custo = valor_custo.replace(',', '.')
        lista_valores_custo.append(valor_custo)
        START_VALOR_CUSTO_Y = START_VALOR_CUSTO_Y + 22

    # Cálculo valor Preço De e Preço Por
    lista_valores_preco_de = []
    lista_valores_preco_por = []
    for valor in lista_valores_custo:
        if valor != '0.00':
            # Markup
            valor = float(valor)
            valor_por = valor * 3
            valor_de = valor * 4

            # Convertendo o preço em uma lista de string
            valor_custo_string_por = str(valor_por)
            valor_custo_string_de = str(valor_de)

            digitos_lista_por = [*valor_custo_string_por]
            digitos_lista_de = [*valor_custo_string_de]

            index_ponto_por = digitos_lista_por.index('.')
            valor_alterar_pre_por = index_ponto_por - 1
            valor_alterar_pos_por = index_ponto_por + 1

            index_ponto_de = digitos_lista_de.index('.')
            valor_alterar_pre_de = index_ponto_de - 1
            valor_alterar_pos_de = index_ponto_de + 1

            # Pegando o segundo digito
            if digitos_lista_por[valor_alterar_pre_por] == '0' or digitos_lista_por[valor_alterar_pre_por] == '5' or \
                    digitos_lista_por[
                        valor_alterar_pre_por] == '6' or digitos_lista_por[valor_alterar_pre_por] == '7' or \
                    digitos_lista_por[
                        valor_alterar_pre_por] == '8' or digitos_lista_por[valor_alterar_pre_por] == '9':
                digitos_lista_por[valor_alterar_pre_por] = '9'

            if digitos_lista_por[valor_alterar_pre_por] == '1' or digitos_lista_por[valor_alterar_pre_por] == '2' or \
                    digitos_lista_por[
                        valor_alterar_pre_por] == '3' or digitos_lista_por[valor_alterar_pre_por] == '4':
                digitos_lista_por[valor_alterar_pre_por] = '4'

            if digitos_lista_de[valor_alterar_pre_de] == '0' or digitos_lista_de[valor_alterar_pre_de] == '5' or \
                    digitos_lista_de[
                        valor_alterar_pre_de] == '6' or digitos_lista_de[valor_alterar_pre_de] == '7' or \
                    digitos_lista_de[
                        valor_alterar_pre_de] == '8' or digitos_lista_de[valor_alterar_pre_de] == '9':
                digitos_lista_de[valor_alterar_pre_de] = '9'

            if digitos_lista_de[valor_alterar_pre_de] == '1' or digitos_lista_de[valor_alterar_pre_de] == '2' or \
                    digitos_lista_de[
                        valor_alterar_pre_de] == '3' or digitos_lista_de[valor_alterar_pre_de] == '4':
                digitos_lista_de[valor_alterar_pre_de] = '4'

            # Alterando o 128.'9'
            digitos_lista_por[valor_alterar_pos_por] = '9'
            digitos_lista_de[valor_alterar_pos_de] = '9'

            valor_por_final = ''.join(digitos_lista_por)
            valor_pre_final = ''.join(digitos_lista_de)

            # Float To String
            valor_por_final = str(valor_por_final).replace('.', ',')
            valor_pre_final = str(valor_pre_final).replace('.', ',')
        else:
            valor_por_final = '0,00'
            valor_pre_final = '0,00'

        lista_valores_preco_por.append(valor_por_final)
        lista_valores_preco_de.append(valor_pre_final)

    # Preenchendo Preço De
    START_PRECO_DE = 187
    pg.moveTo(1510, 165)
    pg.click()
    for valor_preco_de in lista_valores_preco_de:
        pyperclip.copy(valor_preco_de)
        pg.hotkey('ctrl', 'v')
        pg.moveTo(1510, START_PRECO_DE)
        pg.click()
        START_PRECO_DE = START_PRECO_DE + 22

    # Preenche Preço Por
    START_PRECO_POR = 187
    pg.moveTo(1610, 165)
    pg.click()
    for valor_preco_por in lista_valores_preco_por:
        pyperclip.copy(valor_preco_por)
        pg.hotkey('ctrl', 'v')
        pg.moveTo(1610, START_PRECO_POR)
        pg.click()
        START_PRECO_POR = START_PRECO_POR + 22

    stop = stop + 1
