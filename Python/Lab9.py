import json
import requests

# script to print based on user color choice
#print('Please enter your preferred color:')
#color=input()
#r=requests.get('http://localhost:3000/%s' %color)
#data=r.json()
#print(data[0]['color'])

# script to print all colors

qry=requests.get('http://localhost:3000/')
mydata=qry.json()
for i in range(0,4):
    print(mydata[i]['name']+ ' is ' + mydata[i]['color']+ '.')