import os
from time import sleep
from tkinter import messagebox
from ctypes import windll
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


def login_aton(login, senha):
    # Campo de Usuário
    pg.moveTo(1583, 532)
    pg.click()
    pg.typewrite(login)

    # Campo de Senha
    pg.moveTo(1606, 563)
    pg.click()
    pg.typewrite(senha)

    # Botão de Login
    pg.moveTo(1550, 601)
    pg.doubleClick()

    sleep(5)


def button_close_aton():
    # Button Close Ambar
    pg.moveTo(1906, 12)
    pg.click()
    sleep(1)


def menu_produtos():
    # Menu Produtos
    pg.moveTo(283, 37)
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


def cadastro_produtos_botao_consultar():
    pg.moveTo(766, 859)
    pg.click()


def cadastro_produtos_botao_alterar():
    pg.moveTo(617, 857)
    pg.click()


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


def consultar_produtos_menu_cod_id():
    pg.moveTo(35, 120)
    pg.click()
    sleep(1)
    pg.click()
    sleep(1)


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
