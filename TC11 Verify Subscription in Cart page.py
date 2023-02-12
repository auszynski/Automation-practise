# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click 'Cart' button
# 5. Scroll down to footer
# 6. Verify text 'SUBSCRIPTION'
# 7. Enter email address in input and click arrow button
# 8. Verify success message 'You have been successfully subscribed!' is visible

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

# 4. Click 'Cart' button
cartbutton = driver.find_element(By.CSS_SELECTOR,'#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(3) > a > i').click()
time.sleep(2)

# 5. Scroll down to footer

label = driver.find_element(By.CSS_SELECTOR,'html')
label.send_keys(Keys.PAGE_DOWN)

time.sleep(2)

# 6. Verify text 'SUBSCRIPTION'

subscription = driver.find_element(By.CSS_SELECTOR,'#footer > div.footer-widget > div > div > div.col-sm-3.col-sm-offset-1 > div > h2')
if subscription.is_displayed():
    print('SUBSCRIPTION is visible')
time.sleep(2)

# 7. Enter email address in input and click arrow button

entermail = driver.find_element(By.CSS_SELECTOR,'#susbscribe_email')
entermail.send_keys('tester11@automation.com')
time.sleep(2)
subbutton = driver.find_element(By.CSS_SELECTOR,'#subscribe').click()

# 8. Verify success message 'You have been successfully subscribed!' is visible
 
successmsg = driver.find_element(By.CSS_SELECTOR,'#success-subscribe')

if successmsg.is_displayed():
     print('You have been successfully subscribed! is visible')
time.sleep(3)

driver.quit()