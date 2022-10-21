import os
import pyautogui as pg
from time import sleep
import pyperclip


# Funções Auxiliares
def matar_ambar():
    try:
        # Kill Ambar
        os.system("taskkill /im Ambar.exe")
        os.system("taskkill /im Ambar.exe")
    except:
        print('Ambar não está aberto.')


def minimiza_janelas(janela, main):
    # Minimiza o Tkinter
    main.iconify()
    janela.iconify()

    # Minimiza todas as abas
    pg.hotkey('winleft', 'd')

    pg.FAILSAFE = False


def executa_icone_aton():
    # Icone do Aton
    pg.moveTo(36, 100)
    sleep(1)
    pg.doubleClick()

    sleep(1)


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


def cadastro_produtos_seta_grupo():
    pg.moveTo(707, 538)
    pg.click()


def cadastro_produtos_descricao():
    pg.moveTo(633, 684)
    pg.click()


def cadastro_produtos_botao_salvar():
    pg.moveTo(1283, 855)
    # pg.click()


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
    pg.typewrite(['backspace', 'backspace', 'backspace', 'backspace', 'backspace'])


def consultar_produtos_botao_consultar():
    pg.moveTo(632, 61)
    pg.click()
    sleep(1)

def consultar_produtos_select_resultado():
    pg.moveTo(708, 144)
    pg.doubleClick()
    sleep(2)

###################################################
