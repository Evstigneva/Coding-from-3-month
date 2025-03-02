from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.artbreeder.com/tools/prompter'
driver = webdriver.Chrome()
driver.get(url)

element = driver.find_element(By.CSS_SELECTOR, 'textarea[class *= suggest-input]')
print(element)
time.sleep(500000)
element.clear()
time.sleep(5)
element.send_keys('black cat with red and white hat')
element2 = driver.find_element(By.CSS_SELECTOR, 'button[class *= role-emphasized]')
element2.click()
time.sleep(5)
element3 = driver.find_element(By.CSS_SELECTOR, 'img[class *= rounded-2xl]')
print('Time')
time.sleep(5000000000)