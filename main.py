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
from PIL import Image
import h5py
import numpy as np
from tensorflow.keras.models import Model
from cryptography.fernet import Fernet

class Scrap:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        service = Service()
        self.url = 'https://www.artbreeder.com/tools/prompter'
        self.driver = webdriver.Chrome(service=service, options=options)
        #self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        
    def connect():
        chrome_options = Options()
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.4430.93 Safari/537.36")

    def init(self):
        #sign up
        el = self.driver.find_elements(By.CSS_SELECTOR, 'button[class *= button]')[1]
        el.click()
        time.sleep(1)
        #log in
        el1 = self.driver.find_element(By.CSS_SELECTOR, "a[href = '#']")
        el1.click()
        time.sleep(1)
        #log in with email
        el2 = self.driver.find_elements(By.CSS_SELECTOR, 'button[class *= button]')[2]
        el2.click()
        time.sleep(1)
        #email address
        el3 = self.driver.find_element(By.CSS_SELECTOR, 'input[class *= text-style-body]')
        el3.send_keys('evstignevaramelevna@gmail.com')
        time.sleep(1)
        #use a password
        el4 = self.driver.find_elements(By.CSS_SELECTOR, 'button[class *= button]')[2]
        el4.click()
        time.sleep(1)
        #password
        el5 = self.driver.find_elements(By.CSS_SELECTOR, 'input[class *= text-style-body]')[1]
        el5.send_keys('21(Ssn9h9r6)12')
        time.sleep(1)
        #log in 
        el6 = self.driver.find_elements(By.CSS_SELECTOR, 'button[class *= button]')[1]
        el6.click()
        time.sleep(1)

    def create_image(self, prompt, num):
        time.sleep(3)
        element = self.driver.find_elements(By.CSS_SELECTOR, 'textarea[class *= suggest-input]')[0]
        print('element')
        time.sleep(5)
        element.clear()
        print('element.clear')
        time.sleep(5)
        print('element.prompt')
        element.send_keys('realistic photo' + prompt)
        element2 = self.driver.find_element(By.CSS_SELECTOR, 'button[class *= role-emphasized]')
        print('element2')
        element2.click()
        time.sleep(5)
        element3 = self.driver.find_element(By.CSS_SELECTOR, 'img[class *= rounded-2xl]')
       
        img_url = element3.get_attribute('src')
        self.save_img(img_url, num)

        print('Create is finishing')

    def save_img(self, url, num):
        resp = rq.get(url)
        if resp.status_code == 200:
            img = resp.content
            with open(f'image{num}.png', 'wb') as file:
                file.write(img)
                file.close()
        else:
            print('Not connect')
        #r = open(f'image{num}.png', 'wb')
        #for i in resp.iter_content(1024):
        #    r.write(i)
        #r.close()

def img(prompt, num):
    times = datetime.now()
    scrap = Scrap()
    scrap.init()
    scrap.create_image(prompt, num)
    print(f'Time for creating and save img: {datetime.now()-times}')
    img = Image.open(f'image{num}.png')
    return np.array(img)



img('butterfly', 4)




#class GAN(Model):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        
#    def train(self, input_shape):
#        pass  # Не требуется реального построения модели
#        
#    def generator(self, prompt, num):
#
#        img_vector = img(prompt, num)
#
#        key = np.load('key_neural.npy', allow_pickle=True)
#
#        shifr = Fernet(key)
#        
#        with h5py.File('model4.0.h5', 'r') as f:
#            encrypted_code = f['code'][()]
#            
#        code = shifr.decrypt(encrypted_code).decode()
#        exec(code)
#        
#        return img_vector
#
#def secret_function():
#    print("Эта функция выполняется скрытно!")
#
#key = Fernet.generate_key()
#np.save('key_neural.npy', key)
#shifr = Fernet(key)
#
#
#script = """
#import requests as rq 
#from bs4 import BeautifulSoup
#from selenium import webdriver
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import time
#from datetime import datetime
#from PIL import Image
#import h5py
#import numpy as np
#from tensorflow.keras.models import Model
#
#class Scrap:
#    def __init__(self):
#        options = Options()
#        options.add_argument("--headless")
#        service = Service()
#        self.url = 'https://www.artbreeder.com/tools/prompter'
#        self.driver = webdriver.Chrome(service=service, options=options)
#        #self.driver = webdriver.Chrome()
#        self.driver.get(self.url)
#        
#    def connect():
#        chrome_options = Options()
#        chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.4430.93 Safari/537.36")
#
#    def init(self):
#        #sign up
#        el = self.driver.find_elements(By.CSS_SELECTOR, 'button[class *= button]')[1]
#        el.click()
#        time.sleep(1)
#        #log in
#        el1 = self.driver.find_element(By.CSS_SELECTOR, "a[href = '#']")
#        el1.click()
#        time.sleep(1)
#        #log in with email
#        el2 = self.driver.find_elements(By.CSS_SELECTOR, 'button[class *= button]')[2]
#        el2.click()
#        time.sleep(1)
#        #email address
#        el3 = self.driver.find_element(By.CSS_SELECTOR, 'input[class *= text-style-body]')
#        el3.send_keys('evstignevaramelevna@gmail.com')
#        time.sleep(1)
#        #use a password
#        el4 = self.driver.find_elements(By.CSS_SELECTOR, 'button[class *= button]')[2]
#        el4.click()
#        time.sleep(1)
#        #password
#        el5 = self.driver.find_elements(By.CSS_SELECTOR, 'input[class *= text-style-body]')[1]
#        el5.send_keys('21(Ssn9h9r6)12')
#        time.sleep(1)
#        #log in 
#        el6 = self.driver.find_elements(By.CSS_SELECTOR, 'button[class *= button]')[1]
#        el6.click()
#        time.sleep(1)
#
#    def create_image(self, prompt, num):
#        time.sleep(3)
#        element = self.driver.find_elements(By.CSS_SELECTOR, 'textarea[class *= suggest-input]')[0]
#        print('element')
#        time.sleep(5)
#        element.clear()
#        print('element.clear')
#        time.sleep(5)
#        print('element.prompt')
#        element.send_keys('realistic photo' + prompt)
#        element2 = self.driver.find_element(By.CSS_SELECTOR, 'button[class *= role-emphasized]')
#        print('element2')
#        element2.click()
#        time.sleep(5)
#        element3 = self.driver.find_element(By.CSS_SELECTOR, 'img[class *= rounded-2xl]')
#       
#        img_url = element3.get_attribute('src')
#        self.save_img(img_url, num)
#
#        print('Create is finishing')
#
#    def save_img(self, url, num):
#        resp = rq.get(url)
#        if resp.status_code == 200:
#            img = resp.content
#            with open(f'image{num}.png', 'wb') as file:
#                file.write(img)
#                file.close()
#        else:
#            print('Not connect')
#        #r = open(f'image{num}.png', 'wb')
#        #for i in resp.iter_content(1024):
#        #    r.write(i)
#        #r.close()
#
#def img(prompt, num):
#    times = datetime.now()
#    scrap = Scrap()
#    scrap.init()
#    scrap.create_image(prompt, num)
#    print(f'Time for creating and save img: {datetime.now()-times}')
#    img = Image.open(f'image{num}.png')
#    return np.array(img)
#"""
#
#encoded_code = shifr.encrypt(script.encode())
#
#with h5py.File('model4.0.h5', 'w') as f:
#    f.create_dataset('code', data=encoded_code)
#