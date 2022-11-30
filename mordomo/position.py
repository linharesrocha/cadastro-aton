import pyautogui
import time

print('ESCREVA O NOME DA FUNCIONALIDADE: ')
while True:
    response = input()
    if response != '':
        xCursor = pyautogui.position().x
        yCursor = pyautogui.position().y

        print('def ' + response + '():')
        print('    pg.moveTo({0}, {1})'.format(xCursor, yCursor))
        print('    pg.click()')
        print('')
        print('')
    else:
        break