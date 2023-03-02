import pyautogui
from time import sleep

print('ESCREVA O NOME DA FUNCIONALIDADE: ')
while True:
    xCursor = pyautogui.position().x
    yCursor = pyautogui.position().y
    print('pg.moveTo({0}, {1})'.format(xCursor, yCursor))
    sleep(0.2)