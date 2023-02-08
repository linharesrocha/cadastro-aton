import pandas as pd
import pyperclip
import pyautogui as pg


data = pd.read_excel('excel/magalu_madz-precos.xlsx')


pg.moveTo(1726, 169) # preco por
# pg.moveTo(1627, 165) # preco de
pg.click()
pg.press('down')
pg.press('up')
for i in range(len(data)):
    # preco = str(data['PRECO_DE'][i]).replace('.', ',')
    preco = str(data['PRECO_POR'][i]).replace('.', ',')
    pyperclip.copy(preco)
    pg.hotkey('ctrl', 'v')
    pg.press('enter')
    pg.press('down')
    print(str(i + 1) + '/' + str(len(data)))



