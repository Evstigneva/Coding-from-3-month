import numpy as np
import selenium
import os
import requests as rq 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import subprocess

class Dataset:
    def __init__(self):
        self.url = 'https://ru.pinterest.com/'
        
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        y = int(input())

    def find(self, prompt, status):
        self.prompt = prompt
        self.search = self.driver.find_elements(By.CSS_SELECTOR, 'input[class *= w-full]')[0]
        time.sleep(2)
        self.search.clear()
        time.sleep(2)
        self.search.send_keys(status + ' style image ' + prompt)
        time.sleep(2)
        self.but = self.driver.find_elements(By.CSS_SELECTOR, 'button[class *= w-full]')[1]
        time.sleep(2)
        self.but.click()
        time.sleep(2)
        element3 = self.driver.find_elements(By.CSS_SELECTOR, 'img[class *= absolute]')
        time.sleep(2)
        self.prompt = self.prompt.replace(' ', '_')
        print(self.prompt)

        #for i in range(len(element3))[:10]:
        #    img_url = element3[i].get_attribute('src')
        #    self.save_img(img_url, i+1, prompt, status)
        
        if len(element3)>100:
            for i in range(len(element3))[:100]:
                img_url = element3[i].get_attribute('src')
                self.save_img(img_url, i+1, prompt, status)
        
        else:
            for i in range(len(element3)):
                img_url = element3[i].get_attribute('src')
                self.save_img(img_url, i+1, prompt, status)


    def save_img(self, url, num, prompt, status):
        resp = rq.get(url)
        if resp.status_code == 200:
            img = resp.content
            with open(f'/home/evstigneva/proda/craion_dataset_giga/{status}/{prompt}_{num}.png', 'wb') as file:
                file.write(img)
                file.close()
        else:
            print('Not connect')

    def save_dataset(self, num):

        file = np.load('ann_craion.npy', allow_pickle = True).tolist()
        print('File was open')
        time.sleep(5)
        fraze_list = self.driver.find_elements(By.CSS_SELECTOR, 'img[class *=absolute]')
        print('fraze_list')
        time.sleep(5)

        for i in range(len(fraze_list)):
            fraze = fraze_list[i].get_attribute('alt')
            if fraze not in file:
                print(fraze)
                file.append(fraze)
                print(f'{num}:{i}')
            
            elif fraze in file:
                print(fraze)

        np.save('ann_craion.npy', file)


file = np.load('ann_giga.npy', allow_pickle = True)
chet = np.load('chet_giga.npy', allow_pickle = True)

date = Dataset()
try:
    for i in file[chet:]:
        chet+=1
        print(i)
        #if len(list(i.split()))>3:
        #    timing = datetime.now()
        #    date.find(i, 'mult')
        #    print(f'Time for saving picture in style mult: {datetime.now()-timing}')
            

        timing = datetime.now()
        date.find(i, 'realistik')
        print(f'Time for saving picture in style realistik: {datetime.now()-timing}')
        time.sleep(1)
        timing = datetime.now()
        date.find(i, 'mult')
        print(f'Time for saving picture in style mult: {datetime.now()-timing}')
        time.sleep(1)
        timing = datetime.now()
        date.find(i, 'magic')
        print(f'Time for saving picture in style magic: {datetime.now()-timing}')
        time.sleep(1)

except:
    np.save('chet_giga.npy', chet-1)
    date.driver.close()
    date.driver.quit()
    command = ['python', '/home/evstigneva/proda/dataset_on_craion.py']
    result = subprocess.run(command)

date.driver.close()
date.driver.quit()









































#evstignevaramelevna@gmail.com

#21(Ssn9h9r6)12