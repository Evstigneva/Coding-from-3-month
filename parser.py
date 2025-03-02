import os
import requests as rq
from bs4 import BeautifulSoup

url = 'https://opt-opt-opt.ru/'

headers = ''
resp = rq.get(url, headers)

soup = BeautifulSoup(resp.text, 'lxml') #html.parser

data = soup.find('body')
data1 = data.find('div', id = 'wrapper')
data2 = data1.find('div', id = 'content')
data3 = data2.find('div', class_ = 'right_sec')
data4 = data3.find('div', class_ = 'wht_sec')
data5 = data4.find('div', class_ = "bx_catalog_list_home col3 bx_blue")
data6 = data5.find('div',  class_ = "bx_catalog_item double")
data7 = data6.find('div', class_ = "bx_catalog_item_container")
data8 = data7.find('a', id = 'bx_3966226736_593033_pict')
url = 'https://opt-opt-opt.ru' + data7.find('a', class_ = 'bx_catalog_item_images').get('href')
print(url)











def save_img(url, num):
    resp = rq.get(url, stream = True)
    r = open(f'image{num}.png', 'wb')
    for i in resp.iter_content(1024):
        r.write(i)
    r.close()

