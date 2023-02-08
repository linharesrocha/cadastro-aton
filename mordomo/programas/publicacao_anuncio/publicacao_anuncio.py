import pyperclip
import sys
sys.path.append('C:\workspace\cadastro-aton\mordomo')
from auxiliar import *
from login import *

matar_ambar()
executa_icone_aton()
login_aton()
sleep(6)
menu_integracao()
opcao_publicar_anuncio()
publicar_anuncio_filtro_verde()
publicar_anuncio_seleciona_seta_grupo()
publicar_anuncio_seleciona_pisste_grupo()
publicar_anuncio_seleciona_marketplace_magalu_madz()
publicar_anuncio_estoque_positivo()
publicar_anuncio_botao_consultar()
publicar_anuncio_clica_filtro_existe()
publicar_anuncio_aba_produtos_selecionados()
publicar_anuncio_aba_produtos_selecionados_asterisco()
publicar_anuncio_aba_produtos_selecionados_asterisco_auto_id()
publicar_anuncio_produtos_selecionado_remove_filtros_ruins()
publicar_anuncio_aba_produtos_selecionados_filtro_auto_id()


stop = 0
quantidade_produtos = 36
# Preenche nomes
print('PREENCHENDO NOMES.')
while stop < quantidade_produtos:
    print(str(stop + 1) + '/' + str(quantidade_produtos))
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

    FIX_MOVE = 20
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
                START = START + 20
                verification = 1
            else:
                verification = 0
        else:
            verification = 0

    # Preenche Nome
    pg.moveTo(825, 165)
    pg.click()
    pyperclip.copy(titulo_produto)
    for i in range(qntd_variacoes):
        pg.hotkey('ctrl', 'v')
        pg.press('enter')
        pg.press('down')

    # Salvando
    stop = stop + 1