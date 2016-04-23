# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:44:46 2016

@author: thomascoler
"""

import urllib
import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import lxml
import html5lib

def Save_html(url):
    Page_Response = urllib.request.urlopen(url)
    html = Page_Response.read()
    Page_Response.close()
    return html

def Soup_creator(html):
    soup = BeautifulSoup(html, 'html5lib')
    return soup
    
def Find_data(soup, html_element, html_class):
    result = soup.findAll(html_element, {'class':html_class})
    return result

def CSV_write(filename, data):
    f = open(filename, 'a')
    file_write = csv.writer(f)
    file_write.writerow(data)
    f.close()

def Create_file(filename):
    f = open(filename, 'w')
    f.close()
    
    
def Main_function():
    wiki_result = []
    html = Save_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = Soup_creator(html)
    wiki = Find_data(soup, 'table', 'wikitable')[0]  #soup cannot read spaces
    wiki_rows = wiki.findAll('tr')
    for row in wiki_rows:
        wiki_column_result = [wiki_column.text for wiki_column in row.findAll('td')]
        wiki_result.append(wiki_column_result)
        
    Create_file('sp500new.csv')
    

    del wiki_result[0]
    CSV_write('sp500new.csv', ['Ticker Symbol', 'Security', 'SEC filings', 'GICS Sector', 'GICS Sub Industry', 'Address of Headquarters', 'Date first added', 'CIK'])
    for row in wiki_result:
        print (row)
        CSV_write('sp500new.csv', row)
        
Main_function()

print ('The program completed.')


#  result = tree.xpath('//td[contains(text(), "'+'Diluted EPS'+'")]/following-sibling::td[1]/text()')  ->  xpath using xlml to get EPS from key stats



