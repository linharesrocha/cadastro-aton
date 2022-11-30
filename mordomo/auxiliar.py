import os
from time import sleep
from tkinter import messagebox
import pyautogui as pg


# Funções Auxiliares
def matar_ambar():
    try:
        # Kill Ambar
        os.system("taskkill /im Ambar.exe")
        os.system("taskkill /im Ambar.exe")
    except:
        print('Ambar não está aberto.')


def minimiza_janelas(main, janela=0):
    # Mensagem de Atenção
    mensagem_atencao()

    # Minimiza o Tkinter
    main.iconify()
    if janela != 0:
        janela.iconify()

    # Minimiza todas as abas
    pg.hotkey('winleft', 'd')

    pg.FAILSAFE = False


def mensagem_atencao():
    messagebox.showwarning(title='Atenção!', message='Mantenha a mão fora do mouse, e pressione ENTER para iniciar.')


def executa_icone_aton():
    sleep(1)
    # Icone do Aton
    os.startfile("C:\Ambar\Ambar.exe")
    sleep(2)


def button_close_aton():
    # Button Close Ambar
    pg.moveTo(1906, 12)
    pg.click()
    sleep(1)


def menu_integracao():
    pg.moveTo(474, 39)
    pg.click()


def opcao_publicar_anuncio():
    pg.moveTo(517, 270)
    pg.click()
    sleep(1)


def publicar_anuncio_filtro_verde():
    pg.moveTo(881, 84)
    pg.click()


def publicar_anuncio_seleciona_seta_grupo():
    pg.moveTo(410, 127)
    pg.click()


def publicar_anuncio_seleciona_madz_grupo():
    pg.moveTo(283, 189)
    pg.click()


def publicar_anuncio_seleciona_leal_grupo():
    pg.moveTo(276, 170)
    pg.click()


def publicar_anuncio_seleciona_pisste_grupo():
    pg.moveTo(262, 205)
    pg.click()


def publicar_anuncio_seleciona_marktplace_magalu_madz():
    pg.moveTo(152, 408)
    pg.click()


def publicar_anuncio_seleciona_marketplace_magalu_leal():
    pg.moveTo(125, 372)
    pg.click()


def publicar_anuncio_seleciona_marketplace_b2w_leal():
    pg.moveTo(78, 283)
    pg.click()


def publicar_anuncio_seleciona_marketplace_b2w_madz():
    pg.moveTo(104, 184)
    pg.click()


def publicar_anuncio_seleciona_marketplace_shopee_leal():
    pg.moveTo(108, 643)
    pg.click()


def publicar_anuncio_seleciona_marketplace_shopee_madz():
    pg.moveTo(110, 6)
    pg.click()


def publicar_anuncio_seleciona_marketplace_shopee_pisste():
    pg.moveTo(117, 702)
    pg.click()


def publicar_anuncio_seleciona_marketplace_netshoes_leal():
    pg.moveTo(95, 556)
    pg.click()


def publicar_anuncio_seleciona_marketplace_netshoes_madz():
    pg.moveTo(124, 580)
    pg.click()


def publicar_anuncio_seleciona_marketplace_netshoes_pisste():
    pg.moveTo(119, 612)
    pg.click()


def publicar_anuncio_estoque_positivo():
    pg.moveTo(176, 180)
    pg.click()


def publicar_anuncio_botao_consultar():
    pg.moveTo(676, 80)
    pg.click()
    sleep(4)


def publicar_anuncio_clica_filtro_existe():
    pg.moveTo(318, 240)
    pg.click()


def publicar_anuncio_seleciona_resultado_botao_direito():
    sleep(2)
    pg.moveTo(1146, 280)
    pg.rightClick()


def publicar_anuncio_seleciona_resultado_produto():
    pg.moveTo(1201, 316)
    pg.click()
    sleep(3)


def publicar_anuncio_seleciona_resultado_f2():
    pg.moveTo(1211, 296)
    pg.click()
    sleep(1)


def publicar_anuncio_aba_produtos_selecionados():
    pg.moveTo(320, 34)
    pg.click()


def publicar_anuncio_aba_produtos_selecionados_filtro_id():
    pg.moveTo(277, 130)
    pg.click()


def publicar_anuncio_aba_consulta_produtos():
    pg.moveTo(107, 33)
    pg.click()


def publicar_anuncio_aba_produtos_selecionados_asterisco():
    pg.moveTo(7, 132)
    pg.click()


def publicar_anuncio_aba_produtos_selecionados_asterisco_tudo():
    pg.moveTo(15, 172)
    pg.click()


def publicar_anuncio_aba_produtos_selecionados_asterisco_auto_id():
    pg.moveTo(10, 216)
    pg.click()


def publicar_anuncio_aba_produtos_selecionados_filtro_auto_id():
    pg.moveTo(32, 133)
    pg.doubleClick()
    pg.click()


def publicar_anuncio_produtos_selecionado_remove_filtros_ruins():
    pg.moveTo(8, 488)
    pg.click()

    pg.moveTo(13, 569)
    pg.click()

    pg.moveTo(13, 589)
    pg.click()

    pg.moveTo(13, 609)
    pg.click()

    pg.moveTo(13, 634)
    pg.click()

    pg.moveTo(13, 659)
    pg.click()

    pg.moveTo(13, 680)
    pg.click()

    pg.moveTo(13, 700)
    pg.click()

    pg.moveTo(13, 720)
    pg.click()

    pg.moveTo(11, 757)
    pg.click()

    pg.moveTo(11, 822)
    pg.click()

    pg.moveTo(13, 886)
    pg.click()

    pg.moveTo(13, 740)
    pg.click()

    pg.moveTo(13, 864)
    pg.click()


def publicar_anuncio_produtos_selecionado_sobe_barra():
    sleep(1)
    pg.moveTo(1904, 140)
    for i in range(40):
        pg.tripleClick()


def publicar_anuncio_aba_produtos_sobe_barra():
    pg.moveTo(1900, 258)
    for i in range(40):
        pg.tripleClick()


def menu_produtos():
    pg.moveTo(283, 37)
    pg.click()


def publicar_anuncio_aba_selecionados_valor_preco_de():
    pg.moveTo(1472, 162)
    pg.click()


def publicar_anuncio_aba_selecionados_valor_preco_por():
    pg.moveTo(1567, 162)
    pg.click()


def cadastro_produtos_aba_cadastro_produtos():
    pg.moveTo(546, 221)
    pg.click()


def opcao_cadastro_produtos():
    # Cadastro de produtos
    pg.moveTo(328, 60)
    pg.click()

    sleep(2)


# CADASTRO PRODUTOS
def cadastro_produtos_botao_novo():
    pg.moveTo(519, 853)
    pg.click()


def cadastro_produtos_codigo_interno():
    pg.moveTo(681, 261)
    pg.click()


def cadastro_produtos_nome_produto():
    pg.moveTo(905, 316)
    pg.click()


def cadastro_produtos_valor_custo():
    sleep(1)
    pg.moveTo(1087, 589)
    pg.doubleClick()


def cadastro_produtos_ean():
    pg.moveTo(1143, 261)
    pg.click()


def cadastro_produtos_peso():
    pg.moveTo(533, 370)
    pg.click()


def cadastro_produtos_altura():
    pg.moveTo(622, 368)
    pg.click()


def cadastro_produtos_largura():
    pg.moveTo(719, 367)
    pg.click()


def cadastro_produtos_comprimento():
    pg.moveTo(817, 370)
    pg.click()


def cadastro_produtos_ncm():
    pg.moveTo(541, 423)
    pg.click()


def cadastro_produtos_seta_grupo(grupo_info):
    pg.moveTo(707, 538)
    pg.click()
    if grupo_info == 'LEAL':
        cadastro_produtos_opcao_grupo_leal()
    if grupo_info == 'MADZ':
        cadastro_produtos_opcao_grupo_madz()
    if grupo_info == 'PISSTE':
        cadastro_produtos_opcao_grupo_pisste()


def cadastro_produtos_opcao_grupo_leal():
    pg.moveTo(812, 575)
    pg.click()


def cadastro_produtos_opcao_grupo_madz():
    pg.moveTo(794, 594)
    pg.click()


def cadastro_produtos_opcao_grupo_pisste():
    pg.moveTo(782, 615)
    pg.click()


def cadastro_produtos_opcao_desmembra_comp():
    pg.moveTo(1311, 328)
    pg.click()


def cadastro_produtos_descricao():
    pg.moveTo(633, 684)
    pg.click()


def cadastro_produtos_botao_salvar():
    pg.moveTo(1283, 855)
    pg.click()
    sleep(2)


def cadastro_produtos_fechar():
    pg.moveTo(1441, 161)
    pg.click()


def cadastro_produtos_botao_consultar():
    pg.moveTo(766, 859)
    pg.click()


def cadastro_produtos_botao_alterar():
    pg.moveTo(617, 857)
    pg.click()
    sleep(1)


def cadastro_produtos_botao_cancelar():
    pg.moveTo(1390, 858)
    pg.click()


## CONSULTAR PRODUTOS

def consultar_produtos_opcao_todos():
    pg.moveTo(1617, 64)
    pg.click()


def consultar_produtos_pesquisa():
    pg.moveTo(353, 61)
    pg.click()
    pg.hotkey('ctrl', 'a')
    pg.typewrite(['backspace'])


def consultar_produtos_botao_consultar():
    pg.moveTo(632, 61)
    pg.click()
    sleep(1)


def consultar_produtos_select_resultado():
    pg.moveTo(708, 144)
    pg.doubleClick()
    sleep(2)


def menu_vendas():
    pg.moveTo(166, 39)
    pg.click()


def vendas_relatorios_gerenciais():
    pg.moveTo(253, 122)
    pg.click()


def vendas_relatorios_vendas_pedidos():
    pg.moveTo(485, 120)
    pg.click()
    sleep(2)


def relatorio_analise_venda_checkbox_abertos():
    pg.moveTo(87, 116)
    pg.click()


def relatorio_analise_venda_botao_consultar():
    pg.moveTo(758, 114)
    pg.click()
    sleep(3)


def relatorio_analise_venda_gerar_relatorio():
    pg.moveTo(1878, 994)
    pg.click()
    sleep(2)


def relatorio_analise_venda_menu_origem():
    pg.moveTo(513, 69)
    pg.click()


def relatorio_analise_venda_opcao_netshoes_madz():
    pg.moveTo(486, 99)
    pg.click()


def consultar_produtos_menu_cod_id():
    pg.moveTo(35, 120)
    pg.click()
    sleep(1)
    pg.click()
    sleep(1)


# Cadastro Produtos Ficha Técnica
def cadastro_produtos_aba_ficha_tecnica():
    # aba_ficha_tecnica
    pg.moveTo(673, 219)
    pg.click()


def cadastro_produtos_aba_variacao():
    pg.moveTo(1057, 220)
    pg.click()


def cadastro_produtos_ficha_tecnica_menu_skyhub():
    pg.moveTo(530, 475)
    pg.click()


def cadastro_produtos_ficha_tecnica_menu_magalu():
    pg.moveTo(527, 355)
    pg.click()


def cadastro_produtos_ficha_tecnica_menu_netshoes():
    pg.moveTo(527, 431)
    pg.click()


def cadastro_produtos_ficha_tecnica_menu_mercadolivre():
    pg.moveTo(522, 413)
    pg.click()


def cadastro_produtos_ficha_tecnica_botao_adicionar():
    pg.moveTo(676, 562)
    pg.click()


def cadastro_produtos_ficha_tecnica_campo_nome():
    pg.moveTo(777, 281)
    pg.click()


def cadastro_produtos_ficha_tecnica_campo_valor():
    pg.moveTo(963, 280)
    pg.click()


def cadastro_produtos_ficha_tecnica_botao_salvar():
    pg.moveTo(735, 559)
    pg.click()


# botao salvar
pg.moveTo(735, 559)


# Cadastro Produtos Composicao
def cadastro_produtos_aba_composicao():
    pg.moveTo(931, 217)
    pg.click()


def cadastro_produtos_composicao_botao_novo():
    pg.moveTo(1227, 354)
    pg.click()


def cadastro_produtos_composicao_pesquisa_codigo():
    pg.moveTo(532, 357)
    pg.click()


def cadastro_produtos_composicao_resultado_produto():
    pg.moveTo(629, 421)
    pg.doubleClick()


def cadastro_produtos_composicao_quantidade():
    pg.moveTo(1153, 358)
    pg.click()


def cadastro_produtos_composicao_botao_salvar():
    pg.moveTo(1312, 353)
    pg.click()


###################################################

# Tela F8

def entrar_na_tela_f8():
    pg.hotkey('f8')
    sleep(3)


def f8_botao_limpar():
    pg.moveTo(982, 101)
    pg.click()


def f8_caixa_pesquisa_pedido():
    pg.moveTo(86, 58)
    pg.click()


def f8_caixa_select_box_pedido():
    pg.moveTo(21, 35)
    pg.click()


def f8_botao_consultar():
    pg.moveTo(871, 97)
    pg.click()
    sleep(1)
    pg.press('enter')
    sleep(8)


def f8_seleciona_resultado_botao_direito():
    pg.moveTo(625, 245)
    pg.rightClick()


def f8_seleciona_opcao_abrir_garantia():
    pg.moveTo(755, 478)
    pg.click()
