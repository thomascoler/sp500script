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


f = open('wiki_sp.csv', 'w')
outfile = csv.writer(f)



sess = requests.Session()
res = sess.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

soup = BeautifulSoup(res.text, 'html.parser')
table = soup.findAll('table')

rows = table[0].findAll('tr')

header = [i.text for i in table[0].findAll('th')]
outfile.writerow(header)

for r in rows[1:]:
    my_row = [ i.text for i in r.findAll('td') ]
    '''
    print (my_row)
    '''
    ticker = my_row[0]
    try:
        time.sleep(1)
        res = requests.get('http://finance.yahoo.com/q/ks?s='+ticker+'+Key+Statistics')
        soup = BeautifulSoup(res.text, 'html.parser')
        price = soup.find('span', {'class':'time_rtq_ticker'})
        
        table = soup.find('td', {'class':'yfnc_modtitlew1'})
        table = table.text.strip()
        
        
        
        
        
        
        
        my_row.append(price.text.strip())
        
        
        
        outfile.writerow(my_row)

        
    except Exception as e: print (e)
    

f.close()









