# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 19:55:56 2016

@author: thomascoler
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.wait = WebDriverWait(driver, 10)
driver.get('http://www.msn.com/en-us/money')

txtbox = driver.wait.until(EC.presence_of_element_located((By.ID, 'finance-autosuggest')))
txtbox.send_keys('STZ')

txtbox.send_keys(Keys.RETURN)

price = driver.wait.until(EC.presence_of_element_located((By.CLASSNAME, 'current-price'))).getText()
print (price)

time.sleep(10)

driver.close()