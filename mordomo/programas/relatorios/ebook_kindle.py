from bs4 import BeautifulSoup
import requests
import os
from pathlib import Path
from dotenv import load_dotenv
import slack
import urllib.request

os.system('cls')

# Env
env_path = Path('C:/workspace/cadastro-aton/mordomo/programas/') / '.env'
load_dotenv(dotenv_path=env_path)

# Slack Client
app = slack.WebClient(token=os.environ['SLACK_TOKEN'])

url = f'https://www.amazon.com.br/b?ie=UTF8&node=9214411011'

user_agent = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/106.0.0.0 Safari/537.36'}

page = requests.get(url, headers=user_agent)
site = BeautifulSoup(page.content, "html.parser")

container = site.find('ol', class_="a-carousel")

products = container.find_all('li', class_="a-carousel-card acswidget-carousel__card")

contador = 1
for product in products:
    print(f'{str(contador)}/{str(len(products))}')
    
    name_product = product.find(class_='a-truncate-full').getText()
    price_product = product.find(class_='a-offscreen').getText()
    rating_product = product.find(class_='acs-product-block__rating__review-count').getText().replace('(','').replace(')','')
    photo_product = product.find('img').get('src')
    link_product = product.find('a').get('href')
    parts = link_product.split('/')
    link_product = '/'.join(parts[:3])
    link_product = 'https://amazon.com.br' + link_product
    
    # Download image
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    new_name = 'imagem-product.jpg'
    urllib.request.urlretrieve(photo_product, os.path.join(download_path, new_name))

    # Seding Test
    app.chat_postMessage(channel='tendencias-test', text=f'------------------------------------------')
    app.files_upload(channels='tendencias-test', file=f'{download_path}\\{new_name}')
    app.chat_postMessage(channel='tendencias-test', text=f'{link_product}\n{name_product}\n{price_product}\n{rating_product} avaliações\n\n')
    
    contador = contador + 1
    os.system('cls')