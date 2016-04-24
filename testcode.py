# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:43:11 2016

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

driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 3)
driver.get('http://www.msn.com/en-us/money')

txtbox = wait.until(EC.presence_of_element_located((By.ID, 'finance-autosuggest')))

txtbox.send_keys('AAPL')  #ticker symbol


txtbox.send_keys(Keys.RETURN)
    
time.sleep(5)
    
currenturl = driver.current_url
currenturl = currenturl.split('?')[0].split('/')[-1].split('.')
stock = currenturl[-2]+'.'+currenturl[-1]
print (stock)
