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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys


def yf_data1(ticker):
    try:
        res = requests.get('http://finance.yahoo.com/q/ks?s='+ticker+'+Key+Statistics')


        soup = BeautifulSoup(res.text, 'html.parser')
        
        price = soup.find('span', {'class':'time_rtq_ticker'})
        price = price.text   #find the price
            
        book = soup.find('td', text='Book Value Per Share (mrq):').parent.find('td', attrs={'class': 'yfnc_tabledata1'})
        book = book.text #find the Book Value Per Share (mrq)

        yfeps = soup.find('td', text='Diluted EPS (ttm):').parent.find('td', attrs={'class': 'yfnc_tabledata1'})  #find the Diluted EPS (ttm)        
        yfeps = yfeps.text
            
    except Exception as e: 
        print (e)              
        yfeps = "na"
        price = "na"
        book = "na"
    return price, book, yfeps

def yf_data2(ticker):
    try:
        res = requests.get('http://finance.yahoo.com/q/ae?s='+ticker+'+Analyst+Estimates')
        
        soup = BeautifulSoup(res.text, 'html.parser')
        
        estnextyr = soup.find('td', text='Avg. Estimate').parent.findAll('td', attrs={'class': 'yfnc_tabledata1'})
        fwdyr = estnextyr[3].text
    except Exception as e: 
        print (e)              
        fwdyr = "na"
    return fwdyr
    
def get_codename(ticker):
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 3)
    driver.get('http://www.msn.com/en-us/money')

    txtbox = wait.until(EC.presence_of_element_located((By.ID, 'finance-autosuggest')))

    txtbox.send_keys(ticker)  #ticker symbol


    txtbox.send_keys(Keys.RETURN)
    
    time.sleep(5)
    
    currenturl = driver.current_url
    currenturl = currenturl.split('?')[0].split('/')[-1].split('.')
    code = currenturl[-2]+'.'+currenturl[-1]
    return code
    
def ann_eps_msn(code):
    res = requests.get('http://www.msn.com/en-us/money/stockdetailsvnext/financials/income_statement/annual/fi-126.1.'+code+'?ver=2.0.5942.29746')
    soup = BeautifulSoup(res.text, 'html.parser')
    msn_yr_eps = soup.find('div', {'class':'table-data-rows'}).findAll('ul')[27].findAll('li')[-1].find('p').text
    return msn_yr_eps
    
def qtr_eps_msn(code):
    res = requests.get('http://www.msn.com/en-us/money/stockdetailsvnext/financials/income_statement/quarterly/fi-126.1.'+code+'?ver=2.0.5942.29746')
    soup = BeautifulSoup(res.text, 'html.parser')
    msn_qtr_eps = soup.find('div', {'class':'table-data-rows'}).findAll('ul')[27].findAll('li')[-1].find('p').text
    return msn_qtr_eps

def book_msn(code):
    res = requests.get('http://www.msn.com/en-us/money/stockdetails/analysis/fi-126.1.'+code)
    soup = BeautifulSoup(res.text, 'html.parser')
    msn_book = soup.findAll('div', {'class':'table-data-rows'})[1].findAll('ul')[5].findAll('li')[-1].find('p').text
    return (msn_book)   
   
f = open('spValue.csv', 'w')
outfile = csv.writer(f)



sess = requests.Session()
res = sess.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

soup = BeautifulSoup(res.text, 'html.parser')
table = soup.findAll('table')

rows = table[0].findAll('tr')

header = [i.text for i in table[0].findAll('th')]
outfile.writerow(header + ['Price', 'Book Value Per Share', 'Diluted EPS ttm', 'Nxt Yr Analyst Est.'])

for r in rows[1:]:
    my_row = [ i.text for i in r.findAll('td') ]
    '''
    print (my_row)
    '''
    ticker = my_row[0]
    print ('Processing'+ticker)
    
    
    
    #code = get_code(ticker)
    
    #msn_qtr_eps = qtr_eps_msn(code)

    
    
    

    

    price, book, yfeps = yf_data1(ticker)

    fwdyr = yf_data2(ticker)
       
        
    my_row.append(price)
    my_row.append(book)     #use index of list to order columns before write to file
    my_row.append(yfeps)   #my_row.extend(output)
    my_row.append(fwdyr)  #my_row + output
        
    outfile.writerow(my_row)
    
    time.sleep(3)

    

f.close()


'''
            my_row.append(price.text.strip())
            my_row.append(book.text.strip())
            my_row.append(yfeps.text.strip())
            my_row.append(fwdyr.text.strip())
            
'''






