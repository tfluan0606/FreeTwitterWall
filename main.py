from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
from bs4 import BeautifulSoup
import time

with open('twitterlogin.json') as f:
    cookies = json.load(f)

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
 
start_url = "https://twitter.com/tfluan0606/status/1643950839680339969"
driver.get(start_url)

for cookie in cookies:
    # this if conditon is for AssertionError
    # check detail on
    # https://stackoverflow.com/questions/64053551/getting-an-assertion-error-assert-cookie-dictsamesite-in-strict-lax-w
    if 'sameSite' in cookie:
        if cookie['sameSite'] != 'Strict':
            cookie['sameSite'] = 'Strict'
    driver.add_cookie(cookie)
driver.refresh()
# need to set sleep for loading elements
time.sleep(1)
elements = driver.find_elements(By.XPATH,"//img[contains(@src,'https://pbs.twimg.com')]")
pics = []
for i in elements:
    url = i.get_attribute('src')
    if "media" in url:
        pics.append(url)
print(pics)
driver.quit()