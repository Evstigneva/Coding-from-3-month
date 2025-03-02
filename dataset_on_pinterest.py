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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image

class Dataset:
    def __init__(self):
        self.url = 'https://ru.pinterest.com/'
        
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def init(self):
        time.sleep(2)
        self.log_in = self.driver.find_elements(By.CSS_SELECTOR, 'div[class *= RCK]')[0]
        time.sleep(2)
        self.log_in.click()
        time.sleep(2)
        self.pochta = self.driver.find_elements(By.CSS_SELECTOR, 'input[class *= D8X]')[0]
        time.sleep(2)
        self.pochta.send_keys('evstignevaramelevna@gmail.com')
        time.sleep(2)
        self.password = self.driver.find_elements(By.CSS_SELECTOR, 'input[class *=D8X]')[1]
        time.sleep(2)
        self.password.send_keys('21(Ssn9h9r6)12')
        time.sleep(2)
        self.but = self.driver.find_elements(By.CSS_SELECTOR, 'button[class *= RCK]')[2]
        time.sleep(2)
        self.but.click()
        time.sleep(2)

    def crut(self):
        self.pro = self.driver.execute_script('window.scrollTo(0, 5000);')

    def ann(self, prompt, status, seria):
        time.sleep(5)
        self.text = self.driver.find_element(By.CSS_SELECTOR, 'input[role *= combobox]')
        time.sleep(2)

        actions = ActionChains(self.driver)
        actions.move_to_element(self.text)
        actions.click()
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        actions.send_keys(Keys.DELETE).perform()

        time.sleep(2)
        self.text.send_keys(status + ' ' + prompt)
        time.sleep(1)
        self.text.send_keys(Keys.ENTER)
        
        time.sleep(2)

    def find_img(self, prompt, status, seria):
        time.sleep(5)
        print(prompt)
        self.picture = self.driver.find_elements(By.CSS_SELECTOR, 'img[class *= hCL]')
        print(len(self.picture))
        if len(self.picture)==0:
            self.ann(prompt, status, seria)
            self.find_img(prompt, status, seria)

        elif len(self.picture)>0:

            for i in range(len(self.picture)):
                img_url = self.picture[i].get_attribute('src')
                self.save_img(img_url, i+1, prompt, status, seria)
        
    def save_img(self, url, num, prompts, status, seria):
        resp = rq.get(url)
        if resp.status_code == 200:
            img = resp.content
            with open(f'/home/evstigneva/proda/pinterest/giga/{status}/{prompts} {seria}.{num}.png', 'wb') as file:
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
chet = np.load('score_giga.npy', allow_pickle = True)


try:
    date = Dataset()
    date.init()

except:
    date.driver.quit()
    time.sleep(60*30)
    command = ['python', '/home/evstigneva/proda/dataset_on_pinterest.py']
    result = subprocess.run(command)

try:

    for i in file[chet:]:
        chet+=1

        date.ann(i, 'realistic', 1)
        date.find_img(i, 'realistic', 1)
        if len(date.picture)<=10:
            date.crut()
            date.find_img(i, 'realistic', 2)


        date.ann(i, 'magic', 1)
        date.find_img(i, 'magic', 1)
        if len(date.picture)<=10:
            date.crut()
            date.find_img(i, 'magic', 2)

        date.ann(i, 'mult', 1)
        date.find_img(i, 'mult', 1)
        if len(date.picture)<=10:
            date.crut()
            date.find_img(i, 'mult', 2)

except:

    date.driver.quit()
    np.save('score_giga.npy', chet-1)
    command = ['python', '/home/evstigneva/proda/dataset_on_pinterest.py']
    result = subprocess.run(command)
    

#for i in file[chet:]:
#    chet+=1
#    print(i)
#    #if len(list(i.split()))>3:
#    #    timing = datetime.now()
#    #    date.find(i, 'mult')
#    #    print(f'Time for saving picture in style mult: {datetime.now()-timing}')
#        
#    timing = datetime.now()
#    date.find(i, 'realistik')
#    print(f'Time for saving picture in style realistik: {datetime.now()-timing}')
#    time.sleep(1)
#    timing = datetime.now()
#    date.find(i, 'mult')
#    print(f'Time for saving picture in style mult: {datetime.now()-timing}')
#    time.sleep(1)
#    timing = datetime.now()
#    date.find(i, 'magic')
#    print(f'Time for saving picture in style magic: {datetime.now()-timing}')
#    time.sleep(1)


np.save('score_giga.npy', chet-1)
date.driver.close()
date.driver.quit()
#command = ['python', '/home/evstigneva/proda/dataset_on_craion.py']
#result = subprocess.run(command)









































#evstignevaramelevna@gmail.com

#21(Ssn9h9r6)12