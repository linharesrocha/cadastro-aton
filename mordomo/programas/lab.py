import pandas as pd
import pyperclip
import pyautogui as pg

from mordomo.auxiliar import publicar_anuncio_aba_produtos_sobe_barra

#publicar_anuncio_aba_produtos_sobe_barra()
# Muda SKU
stop = 0
pg.moveTo(597, 166)
pg.click()
pg.press('down')
pg.press('up')

while stop < 30:
    pg.hotkey('ctrl', 'c')
    cabecalho = pyperclip.paste()
    lista_valores_cabecalho = cabecalho.split("\t")
    sku = lista_valores_cabecalho[-8]
    sku = sku + '7'
    pyperclip.copy(sku)
    pg.hotkey('ctrl', 'v')
    pg.press('enter')
    pg.press('down')
    stop = stop + 1