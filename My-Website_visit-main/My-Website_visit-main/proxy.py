from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import find_connectable_ip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.proxy import Proxy, ProxyType

options = Options()
options.headless = False




prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "104.43.230.151:3128"
prox.socks_proxy = "24.139.143.226:4153"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

driver = webdriver.Chrome(options=options, executable_path=r'driver.exe')
drive = webdriver.Chrome(desired_capabilities=capabilities)
driver.get('http://www.whatsmyip.org/')