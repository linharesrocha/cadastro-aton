import pyautogui as pg
import os
from pathlib import Path
from time import sleep
from dotenv import load_dotenv

# Load Variables
env_path = Path('..') / 'C:\workspace\cadastro-aton\.env'
load_dotenv(dotenv_path=env_path)
login = os.environ['LOGIN_USER']
senha = os.environ['LOGIN_PASS']


def login_aton():
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

    sleep(6)
