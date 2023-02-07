import pandas as pd
import os

os.system('cls')

data = pd.read_excel('C:/workspace/cadastro-aton/mordomo/programas/excel/ATRIBUTOS_MELI.xlsx')
for i in range(len(data)):
    codid = int(i)
    if codid in set(data['CODID']):
        datatmp = data[data['CODID'] == codid]
        if datatmp["IDTIPO"].isin(["SIZE"]).any() and (~datatmp["IDTIPO"].isin(["COLOR"])).all():
            print(datatmp['CODID'].iloc[0])
        