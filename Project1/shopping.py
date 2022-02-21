from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import pandas as pd

#driver = webdriver.Chrome("/usr/lib/chromium-brower/chromedriver")
print("What are you shopping for...");

mystr=input("Enter a product item that you are shopping for : ");
usr_site=input("Where do you want to shop..amazon/google/etsy/...?");
if usr_site=="amazon":
    mystr="https://www.amazon.com/s?k="+mystr

elif usr_site=="etsy":
    mystr="https://www.etsy.com/search?q="+mystr
else:
    print("shopping in google...")
    mystr="https://www.google.com/search?tbm=shop&hl=en&q="+mystr

op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches',['enable-logging'])
op.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=op, service=Service(ChromeDriverManager().install()))
driver.delete_all_cookies()

driver.get(mystr)
result = requests.get(mystr)

src=result.text
soup=BeautifulSoup(src,"lxml")
