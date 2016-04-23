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

txtbox.send_keys('AAPL')

txtbox.send_keys(Keys.RETURN)

price = driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'current-price'))).text
print (price)

financialurl = driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="financials"]/a'))).get_attribute('href')
financailurl = 'http://www.msn.com/'+financialurl

driver.get (financialurl)

yr_eps = driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="table-content-area"]/div/div/div[1]/div/ul[30]/li[5]/p'))).text

#qrt_tab = driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="financials-period-list"]/li[2]'))).click()

#//*[@id="table-content-area"]/div/div/div[1]/div/ul[30]/li[5]/p
#financials-period-list > li.financials-period-tabs.pointer.active
driver.execute_script('document.getElementsByClassName("financials-period-tabs").setAttribute("class", "active")')
qrt_eps = driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="table-content-area"]/div/div/div[1]/div/ul[30]/li[5]/p'))).text
print (yr_eps)
print (qtr_eps)

time.sleep(20)



driver.close()

