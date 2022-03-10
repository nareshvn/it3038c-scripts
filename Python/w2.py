from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests, re
#r = requests.get('https://analytics.usa.gov').content
#soup=BeautifulSoup(r, "lxml")
#print(type(soup))
#print(soup.prettify()[:100])
#for link in soup.find_all('a'): print(link.get('href'))


r = requests.get('https://www.worldometers.info/coronavirus/#counries').text

soup=BeautifulSoup(r, "lxml")
#span = soup.find('class', {"class":"currency-dashboard__Cell-sc-11c1bd-7 kejAwQ"})
#print(span)

#for link in soup.find_all('table table-bordered table-hover downloads'): print(link.get('td'))


table1=soup.find("table", id ="main_table_countries_today")
heads=[]
col_count=0
for i in table1.find_all("th"):
    title = i.text
    col_count=col_count + 1
    heads.append(title)
    #print (col_count, title)
mydata = pd.DataFrame(columns=heads)
country=[]
counts=[]
for j in table1.find_all('tr')[1:]:
    row_data=j.find_all('td')
    row=[i.text for i in row_data]

    dta=row[1]+ " - " + row[2]
    print(dta)
    #country.append(row[1], " - ", row[2])
    country.append(dta)
    counts.append(row[2])

mydata = pd.DataFrame(columns=country)

mydata.to_csv('covid_data.csv', index=False)
