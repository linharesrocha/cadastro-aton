import pandas as pd

data = pd.read_excel('excel/MAGALU_MADZ.xlsx')
verifica = []
for i in range(len(data)):
    codid = str(data['MATERIAL_ID'][i])
    sku = str(data['SKU'][i])

    verifica.append('S') if codid in sku else verifica.append('N')

data['CHECK'] = verifica
data.to_excel('excel/MAGALU_MADZ_POS.xlsx', index=False)