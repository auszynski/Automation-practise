# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Test Cases' button
# 5. Verify user is navigated to test cases page successfully

from os import system
import time
from pkg_resources import find_distributions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#1. Launch browser

driver = webdriver.Chrome() #browser which we choose
WebDriverWait(driver,10)
time.sleep(1)

#2. Navigate to url 'http://automationexercise.com'

driver.get('http://automationexercise.com') #website that we want to open
WebDriverWait(driver,1)
time.sleep(1) #test wait 3sec after open website

#3. Verify that home page is visible successfully

opensite = driver.find_element(By.ID,'header') #we want verified that the page opened successfully by view header part of home page
time.sleep(1) 
if opensite.is_displayed():                      #We generate comunicate if we open the page successfully or not
    print("The home page is visible successfully!") 

# 4. Click on 'Test Cases' button

testcases = driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a').click()

# 5. Verify user is navigated to test cases page successfully

tcases = driver.find_element(By.XPATH,'//*[@id="form"]/div/div[1]/div/h2/b')

if tcases.is_displayed():
    print('User is navigated to test cases page successfully')

time.sleep(2)
driver.quit()