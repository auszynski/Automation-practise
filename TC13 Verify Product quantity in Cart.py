# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click 'View Product' for any product on home page
# 5. Verify product detail is opened
# 6. Increase quantity to 4
# 7. Click 'Add to cart' button
# 8. Click 'View Cart' button
# 9. Verify that product is displayed in cart page with exact quantity

from os import system
import time
from pkg_resources import find_distributions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


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

# 4. Click 'View Product' for any product on home page

viewproduct = driver.find_element(By.CSS_SELECTOR,'body > section:nth-child(3) > div.container > div > div.col-sm-9.padding-right > div.features_items > div:nth-child(8) > div > div.choose > ul > li > a').click()
time.sleep(3)

# 5. Verify product detail is opened

details = driver.find_element(By.CSS_SELECTOR,'body > section > div > div > div.col-sm-9.padding-right > div.product-details > div.col-sm-7 > div')
if details.is_displayed():
    print('Product details is opened')
time.sleep(1)

# 6. Increase quantity to 4

quantitytab = driver.find_element(By.CSS_SELECTOR,'#quantity')
x = 4
quantitytab.click()
quantitytab.clear()

time.sleep(1)
quantitytab.send_keys(x)
time.sleep(3)

# 7. Click 'Add to cart' button

add = driver.find_element(By.CSS_SELECTOR,'body > section > div > div > div.col-sm-9.padding-right > div.product-details > div.col-sm-7 > div > span > button').click()
time.sleep(1)

# 8. Click 'View Cart' button

viewcart = driver.find_element(By.CSS_SELECTOR,'#cartModal > div > div > div.modal-body > p:nth-child(2) > a').click()
time.sleep(2)

# 9. Verify that product is displayed in cart page with exact quantity

quantityincart = driver.find_element(By.CSS_SELECTOR,'#product-6 > td.cart_quantity')
print('elo', quantityincart.get_attribute('value'))
#quantityincart.is_displayed()
#print(quantityincart.getAttribute('value'))

if x == quantityincart.get_attribute('value'):
    print('Product is displayed in cart page with exact quantity')
time.sleep(4)
driver.quit()
#product-11 > td.cart_quantity > button