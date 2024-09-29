 # -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 03:49:53 2018

@author: jacques
"""
import time
import requests 
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
j=('                Cuz Jacques says so and he controls runs internet yo')

print('               The current price of the one the only Bitcoin is this aint BBBY:   $' + r.json()['bpi']['USD']['rate'])
print(j)
print (r.json()['time']['updated'])