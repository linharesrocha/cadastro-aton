import pandas as pd
from requests import get
from io import BytesIO
from PIL import Image

data = pd.read_excel('excel/verifica_dimensao.xls')

dimensao_1 = []
dimensao_2 = []
dimensao_3 = []
dimensao_4 = []
dimensao_5 = []

print('URL1')
for url in data['url']:
    try:
        image_raw = get(url)
        image = Image.open(BytesIO(image_raw.content))
        width, height = image.size
        dimensao_1.append(str(height) + 'x' + str(width))
    except:
        dimensao_1.append(0)

print('URL2')
for url in data['url2']:
    try:
        image_raw = get(url)
        image = Image.open(BytesIO(image_raw.content))
        width, height = image.size
        dimensao_2.append(str(height) + 'x' + str(width))
    except:
        dimensao_2.append(0)

print('URL3')
for url in data['url3']:
    try:
        image_raw = get(url)
        image = Image.open(BytesIO(image_raw.content))
        width, height = image.size
        dimensao_3.append(str(height) + 'x' + str(width))
    except:
        dimensao_3.append(0)

print('URL4')
for url in data['url4']:
    try:
        image_raw = get(url)
        image = Image.open(BytesIO(image_raw.content))
        width, height = image.size
        dimensao_4.append(str(height) + 'x' + str(width))
    except:
        dimensao_4.append(0)

print('URL5')
for url in data['url5']:
    try:
        image_raw = get(url)
        image = Image.open(BytesIO(image_raw.content))
        width, height = image.size
        dimensao_5.append(str(height) + 'x' + str(width))
    except:
        dimensao_5.append(0)


data['dimensao1'] = dimensao_1

data['dimensao2'] = dimensao_2

data['dimensao3'] = dimensao_3

data['dimensao4'] = dimensao_4

data['dimensao5'] = dimensao_5


data_pronto = data[['cod_id', 'cod_interno', 'url', 'dimensao1',
                    'url2', 'dimensao2', 'url3', 'dimensao3', 'url4', 'dimensao4',
                    'url5', 'dimensao5']]

data_pronto.to_excel('converte_dimensao_download.xls', index=False)
