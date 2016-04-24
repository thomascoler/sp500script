# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:35:09 2016

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

res = requests.get('http://www.msn.com/en-us/money/stockdetails/analysis/fi-126.1.AAPL.NAS')
soup = BeautifulSoup(res.text, 'html.parser')

msn_book = soup.findAll('div', {'class':'table-data-rows'})[1].findAll('ul')[5].findAll('li')[-1].find('p').text
print (msn_book)  