import os
import urllib.request

from PIL import Image
import wget
import pandas as pd

data = pd.read_excel('excel/converte_dimensao_download.xls')

aux = 0
for id in data['cod_id']:
    print(str(aux) +'/'+ str(len(data)))
    print(id)
    url = data['url'][aux]
    print(url)
    try:
        file_name = wget.download(url)
    except:
        file_name = 'image.jpg'
        urllib.request.urlretrieve(url, file_name)

    # Resize image
    image = Image.open(file_name)
    new_image = image.resize((1000, 1000))

    # Salvando imagem
    try:
        new_image.save("C:/DAGG_IMAGES" + '/' + str(id) + '/' + file_name)
    except:
        new_image.save("C:/DAGG_IMAGES" + '/' + str(id) + '/' + file_name + '.jpg')

    # Delete image
    os.remove(file_name)
    aux = aux + 1