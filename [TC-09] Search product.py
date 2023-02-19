# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Products' button
# 5. Verify user is navigated to ALL PRODUCTS page successfully
# 6. Enter product name in search input and click search button
# 7. Verify 'SEARCHED PRODUCTS' is visible
# 8. Verify all the products related to search are visible

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

time.sleep(1)

# 4. Click on 'Products' button

products = driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a').click()

# 5. Verify user is navigated to ALL PRODUCTS page successfully

allproducts = driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/h2')
if allproducts.is_displayed():
    print('User is navigated to ALL PRODUCTS page')
time.sleep(3)
# 6. Enter product name in search input and click search button

searchtab = driver.find_element(By.CSS_SELECTOR,'#search_product')
searchtab.send_keys('Winter Top')

time.sleep(1)

searchbutton = driver.find_element(By.CSS_SELECTOR,'#submit_search').click()
time.sleep(4)

# 7. Verify 'SEARCHED PRODUCTS' is visible

srchprdct = driver.find_element(By.CSS_SELECTOR,'body > section:nth-child(3) > div.container > div > div.col-sm-9.padding-right > div > h2')
if srchprdct.is_displayed():
    print('SEARCHED PRODUCT is visible')
time.sleep(1)
# 8. Verify all the products related to search are visible

searchedproduct = driver.find_element(By.CSS_SELECTOR,'body > section:nth-child(3) > div.container > div > div.col-sm-9.padding-right > div > div.col-sm-4 > div > div.single-products > div.productinfo.text-center')
if searchedproduct.is_displayed():
    print('All related products are visible')
time.sleep(4)

driver.quit()