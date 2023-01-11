import pandas as pd

data = pd.read_excel('excel/Pasta1.xlsx')

lista_de_ean = data['EAN13'].tolist()

aux = 1.0
for ean in lista_de_ean:
    ean = str(ean)
    # Transformando no padrão
    codigo_ean_montagem = ["DG", ean[0], ean[8:], "PAI"]
    codigo_ean_montagem = list(map(str, codigo_ean_montagem))

    # Junta a lista em um código único
    codigo_ean_final = ''.join(codigo_ean_montagem)
    print(codigo_ean_final)