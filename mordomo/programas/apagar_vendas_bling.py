from mordomo.auxiliar import *
import pandas as pd
from time import sleep

for i in range(65):
    # Seleciona filtro
    pg.moveTo(254, 270)
    sleep(1)
    pg.click()
    sleep(2)

    # Lixeira
    pg.moveTo(1645, 206)
    sleep(1)
    pg.click()
    sleep(2)


    # Confirma
    pg.moveTo(1123, 640)
    pg.click()
    sleep(60)