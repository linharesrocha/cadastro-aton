import os
from PIL import Image
import wget
import pandas as pd

data = pd.read_excel('excel/converte_dimensao_download.xls')

aux = 0
for url in data['url']:
    try:
        print(str(aux) +'/'+ str(len(data)))
        # try:
        file_name = wget.download(url)

        # Resize image
        image = Image.open(file_name)
        new_image = image.resize((1000, 1000))

        # Procurando index
        index = data[data['url'] == url].index.values
        index = index[0]
        print('ID: ' + str(index))

        # Salvando imagem
        new_image.save("C:/DAGG_IMAGES" + '/' + str(data['cod_id'][index]) + '/' + file_name)

        # Delete image
        os.remove(file_name)

        aux = aux + 1
    except:
        print('Não consegui.')