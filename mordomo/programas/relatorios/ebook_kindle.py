from bs4 import BeautifulSoup
import pandas as pd
import requests

url = f'https://www.amazon.com.br/b?ie=UTF8&node=9214411011'

user_agent = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/106.0.0.0 Safari/537.36'}

page = requests.get(url, headers=user_agent)
site = BeautifulSoup(page.content, "html.parser")

container = site.find('ol', class_="a-carousel")

products = container.find_all('li', class_="a-carousel-card acswidget-carousel__card")

for product in products:
    name_product = product.find(class_='a-truncate-full').getText()
    price_product = product.find(class_='a-offscreen').getText()
    rating_product = product.find(class_='acs-product-block__rating__review-count').getText().replace('(','').replace(')','')
    photo_product = product.find('img').get('src')
    print(name_product)
    print(price_product)
    print(rating_product)
    print(photo_product)
    break  
