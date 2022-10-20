import pyautogui
import time
time.sleep(2)

print('ESCREVA O NOME DA FUNCIONALIDADE: ')
while True:
    response = input()
    if response != '':
        xCursor = pyautogui.position().x
        yCursor = pyautogui.position().y

        print('# ' + response)
        print('pg.moveTo({0}, {1})'.format(xCursor, yCursor))
    else:
        break