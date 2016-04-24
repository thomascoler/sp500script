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
driver.maximize_window()
wait = WebDriverWait(driver, 3)
driver.get('http://www.msn.com/en-us/money')

txtbox = wait.until(EC.presence_of_element_located((By.ID, 'finance-autosuggest')))

txtbox.send_keys('AAPL')  #ticker symbol


txtbox.send_keys(Keys.RETURN)

price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'current-price'))).text


financialurl = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="financials"]/a'))).get_attribute('href')
financailurl = 'http://www.msn.com/'+financialurl

driver.get (financialurl)

yr_eps = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="table-content-area"]/div/div/div[1]/div/ul[30]/li[5]/p'))).get_attribute('innerHTML')


qtrtab = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="financials-period-list"]/li[2]')))
qtrtab.click()
time.sleep(10)
#//*[@id="table-content-area"]/div/div/div[1]/div/ul[30]/li[5]/p
#financials-period-list > li.financials-period-tabs.pointer.active
#driver.execute_script('document.getElementsByClassName("financials-period-tabs").setAttribute("class", "active")')
qrt_eps = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="table-content-area"]/div/div/div[1]/div/ul[30]/li[5]/p'))).get_attribute('innerHTML')


print (price)
print (yr_eps)
print (qrt_eps)



driver.close()

