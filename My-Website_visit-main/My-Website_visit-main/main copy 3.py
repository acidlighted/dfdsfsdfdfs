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
    driver.get("https://nafiohere.blogspot.com")
    time.sleep(20)
    #ele = driver.find_element_by_xpath("//iframe[@width='160']").click()
    time.sleep(5)
    driver.get("https://nafiohere.blogspot.com/2021/08/thinking-of-keeping-dairy.html")
    time.sleep(5)
    #ele = driver.find_element_by_xpath("//iframe[@width='160']").click()
    time.sleep(2)
    subew = driver.find_element_by_link_text("Happy Days")
    subew.click() 
    time.sleep(5)
    driver.get("https://nafiohere.blogspot.com/2020/07/morning-day.html")
    time.sleep(10)
    #ele = driver.find_element_by_xpath("//iframe[@width='160']").click()
    #elet = driver.find_element_by_xpath("//iframe[@width='300']").click()
    time.sleep(5)
    subew = driver.find_element_by_link_text("Happy Days")
    subew.click() 
    time.sleep(3)
    print("respond" ,end =" ")
    print (i)
    i= i+1 
    
   


    




























