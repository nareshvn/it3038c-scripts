
from flask import Flask, render_template, request
#, flash, redirect, url_for
import os as os
import pandas as pd
#import requests
#from bs4 import BeautifulSoup
sdata = os.uname()
sys_data =[]
sys_data.append(sdata.version)
sys_data.append(sdata.machine)
sys_data.append(sdata.release)
sys_data.append(sdata.sysname)



app=Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def hello():

    myName='Venkat Naresh'
    return render_template("index.html", value=myName)

@app.route('/welcome', methods=['POST'])
def welcome():
    return render_template("welcome.html",
    myName=request.form['myName'],
    shop_for=request.form['shop_for'],
    vendor=request.form['vendor'],
    cCtry=request.form['cCtry'])

@app.route('/table')
def table():
    data=pd.read_csv('countries.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])

@app.route('/sysinfo')
def sysinfo():
    return render_template("sysinfo.html",sys_data=sys_data)
