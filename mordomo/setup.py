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

move_aton_user_x = int(os.environ['MOVE_ATON_USER_X'])
move_aton_user_y = int(os.environ['MOVE_ATON_USER_Y'])

move_aton_pass_x = int(os.environ['MOVE_ATON_PASS_X'])
move_aton_pass_y = int(os.environ['MOVE_ATON_PASS_Y'])

move_aton_button_x = int(os.environ['MOVE_ATON_BUTTON_X'])
move_aton_button_y = int(os.environ['MOVE_ATON_BUTTON_Y'])


def login_aton():
    # Campo de Usuário
    pg.moveTo(move_aton_user_x, move_aton_user_y)
    pg.click()
    pg.typewrite(login)

    # Campo de Senha
    pg.moveTo(move_aton_pass_x, move_aton_pass_y)
    pg.click()
    pg.typewrite(senha)

    # Botão de Login
    pg.moveTo(move_aton_button_x, move_aton_button_y)
    pg.doubleClick()

    sleep(6)
