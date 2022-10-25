import pyautogui as pg
from time import sleep

LOGIN_USER = 'GUI'
LOGIN_PASS = '1234'


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