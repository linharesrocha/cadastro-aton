import pandas as pd
import pyperclip
import pyautogui as pg


data = pd.read_excel('excel/precos-magalu.xlsx')
pg.moveTo(530, 168)
pg.click()
pg.press('down')
pg.press('up')

for i in range(len(data)):
    pg.hotkey('ctrl', 'c')
    cabecalho = pyperclip.paste()
    lista_valores_cabecalho = cabecalho.split("\t")
    sku = lista_valores_cabecalho[-21]
    sku = sku + '1'
    print(sku)
    pyperclip.copy(sku)
    pg.hotkey('ctrl', 'v')
    pg.press('enter')
    pg.press('down')

