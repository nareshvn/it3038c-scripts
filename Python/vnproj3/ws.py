import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import urllib.request

# Set the URL you want to webscrape from
url = "https://www.federalreserve.gov/releases/h10/current/"
# Connect to the URL
with urllib.request.urlopen(url) as i:
    html=i.read()

data=pd.read_html(html)[0]
print(data.head())

data.to_csv("countries.csv")
data1 = pd.read_csv("countries.csv")
df = pd.DataFrame(data1, columns=['COUNTRY','CURRENCY','Apr. 8'])

print(df)
