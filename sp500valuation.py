#! /usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 18:48:33 2016

@author: thomascoler
"""

from bs4 import BeautifulSoup
import requests
import csv, re
import time
import lxml
import random

f = open('spValue.csv', 'w')
outfile = csv.writer(f)



sess = requests.Session()
res = sess.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

soup = BeautifulSoup(res.text, 'html.parser')
table = soup.findAll('table')

rows = table[0].findAll('tr')

header = [i.text for i in table[0].findAll('th')]
outfile.writerow(header + ['Price', 'Book Value Per Share', 'Diluted EPS ttm'])

for r in rows[1:]:
    my_row = [ i.text for i in r.findAll('td') ]
    '''
    print (my_row)
    '''
    ticker = my_row[0]
    print ('Processing'+ticker)
    try:
      
        res = requests.get('http://finance.yahoo.com/q/ks?s='+ticker+'+Key+Statistics')
        soup = BeautifulSoup(res.text, 'html.parser')
        price = soup.find('span', {'class':'time_rtq_ticker'})  #find the price
        book = soup.find('td', text='Book Value Per Share (mrq):').parent.find('td', attrs={'class': 'yfnc_tabledata1'}) #find the Book Value Per Share (mrq) 
        eps = soup.find('td', text='Diluted EPS (ttm):').parent.find('td', attrs={'class': 'yfnc_tabledata1'})  #find the Diluted EPS (ttm)        
        
        '''
        table = soup.find('td', {'class':'yfnc_modtitlew1'})
        table = table.text.strip()
       
        //*[@id="yui_3_9_1_8_1461218085350_49"] ->xpath selector for diluted EPS
        '''
        
        
        
        
        
        
        
        my_row.append(price.text.strip())
        my_row.append(book.text.strip())
        my_row.append(eps.text.strip())
        
        
        
        outfile.writerow(my_row)

        
    except Exception as e: print (e)
    

f.close()









