# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click 'Products' button
# 5. Hover over first product and click 'Add to cart'
# 6. Click 'Continue Shopping' button
# 7. Hover over second product and click 'Add to cart'
# 8. Click 'View Cart' button
# 9. Verify both products are added to Cart
# 10. Verify their prices, quantity and total price

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
time.sleep(4)

# 5. Hover over first product and click 'Add to cart'

first = driver.find_element(By.CSS_SELECTOR,'body > section:nth-child(3) > div.container > div > div.col-sm-9.padding-right > div > div:nth-child(3) > div > div.single-products > div.productinfo.text-center > a').click()
time.sleep(2)

# 6. Click 'Continue Shopping' button

continuebutton = driver.find_element(By.CSS_SELECTOR,'#cartModal > div > div > div.modal-footer > button').click()
time.sleep(2)

# 7. Hover over second product and click 'Add to cart'

second = driver.find_element(By.CSS_SELECTOR,'body > section:nth-child(3) > div.container > div > div.col-sm-9.padding-right > div > div:nth-child(4) > div > div.single-products > div.productinfo.text-center > a').click()
time.sleep(2)

# 8. Click 'View Cart' button

viewcart = driver.find_element(By.CSS_SELECTOR,'#cartModal > div > div > div.modal-body > p:nth-child(2) > a').click()
time.sleep(2)

# 9. Verify both products are added to Cart

firstproduct = driver.find_element(By.CSS_SELECTOR,'#product-1')
secondproduct = driver.find_element(By.CSS_SELECTOR,'#product-2')

if firstproduct.is_displayed() and secondproduct.is_displayed():
    print('Products are visible')
time.sleep(2)

# 10. Verify their prices, quantity and total price

firstprice = driver.find_element(By.CSS_SELECTOR,'#product-1 > td.cart_price > p')
secondprice = driver.find_element(By.CSS_SELECTOR,'#product-2 > td.cart_price > p')
firstquantity = driver.find_element(By.CSS_SELECTOR,'#product-1 > td.cart_quantity')
secondquantity = driver.find_element(By.CSS_SELECTOR,'#product-2 > td.cart_quantity')
firsttotal = driver.find_element(By.CSS_SELECTOR,'#product-1 > td.cart_total')
secondtotal = driver.find_element(By.CSS_SELECTOR,'#product-2 > td.cart_total')

if firstprice.is_displayed() and secondprice.is_displayed() and firstquantity.is_displayed() and secondquantity.is_displayed() and firsttotal.is_displayed() and secondtotal.is_displayed():
    print('Prices, quantity and total price are visible')

time.sleep(2)
driver.quit()