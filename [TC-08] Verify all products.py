# 1. Launch browser.
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Products' button
# 5. Verify user is navigated to ALL PRODUCTS page successfully
# 6. The products list is visible
# 7. Click on 'View Product' of first product
# 8. User is landed to product detail page
# 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand

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
# 6. The products list is visible

productlist = driver.find_element(By.CSS_SELECTOR,'body > section:nth-child(3) > div.container > div > div.col-sm-9.padding-right')

if productlist.is_displayed():
    print('Product list is visible')
time.sleep(2)
# 7. Click on 'View Product' of first product

firstproduct = driver.find_element(By.CSS_SELECTOR,'body > section:nth-child(3) > div.container > div > div.col-sm-9.padding-right > div > div:nth-child(3) > div > div.choose > ul > li > a').click()
time.sleep(1)

# 8. User is landed to product detail page

firstproductdetail = driver.find_element(By.CSS_SELECTOR,'body > section > div > div > div.col-sm-9.padding-right > div.product-details')
if firstproductdetail.is_displayed():
    print('User is landed to product detail prage')

time.sleep(1)

# 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand

name = driver.find_element(By.CSS_SELECTOR,'body > section > div > div > div.col-sm-9.padding-right > div.product-details > div.col-sm-7 > div > h2')
if name.is_displayed():
    print('Name is visible')
time.sleep(1)

category = driver.find_element(By.CSS_SELECTOR,'body > section > div > div > div.col-sm-9.padding-right > div.product-details > div.col-sm-7 > div > p:nth-child(3)')
if category.is_displayed():
    print('Category is visible')
time.sleep(1)

price = driver.find_element(By.CSS_SELECTOR,'body > section > div > div > div.col-sm-9.padding-right > div.product-details > div.col-sm-7 > div > span > span')
if price.is_displayed():
    print('Price is visible')
time.sleep(1)

availability = driver.find_element(By.CSS_SELECTOR,'body > section > div > div > div.col-sm-9.padding-right > div.product-details > div.col-sm-7 > div > p:nth-child(6)')
if availability.is_displayed():
    print('Availability is visible')
time.sleep(1)

condition = driver.find_element(By.CSS_SELECTOR,'body > section > div > div > div.col-sm-9.padding-right > div.product-details > div.col-sm-7 > div > p:nth-child(7) > b')
if condition.is_displayed():
    print('Condition is visible')
time.sleep(1)

brand = driver.find_element(By.CSS_SELECTOR,'body > section > div > div > div.col-sm-9.padding-right > div.product-details > div.col-sm-7 > div > p:nth-child(8)')
if brand.is_displayed():
    print('Brand is visible')
time.sleep(1)

driver.quit()