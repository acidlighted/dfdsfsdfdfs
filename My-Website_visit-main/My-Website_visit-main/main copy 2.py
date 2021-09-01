from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import find_connectable_ip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


i= 1
while i <4:
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(options=options, executable_path=r'driver.exe')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-javascript')
    
    
    
    driver.get('https://nafiohere.blogspot.com/')
    time.sleep(30)
    driver.quit()
    
    print("respond" ,end =" ")
    print (i)
    i= i+1 
    driver.quit()
    
   


    




























