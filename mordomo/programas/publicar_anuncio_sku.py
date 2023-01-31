import pyautogui as pg
import pyperclip

print('MUDANDO SKU...')
# Muda SKU
stop = 0
pg.moveTo(597, 166)
pg.click()
pg.press('down')
pg.press('up')
quantidade_anuncios = 308

while stop < quantidade_anuncios:
    print(str(stop + 1) + '/' + str(quantidade_anuncios))
    pg.hotkey('ctrl', 'c')
    cabecalho = pyperclip.paste()
    lista_valores_cabecalho = cabecalho.split("\t")
    sku = lista_valores_cabecalho[-8]
    print(sku)
    sku = sku + '8'
    print(sku)
    pyperclip.copy(sku)
    pg.hotkey('ctrl', 'v')
    pg.press('enter')
    pg.press('down')
    stop = stop + 1
