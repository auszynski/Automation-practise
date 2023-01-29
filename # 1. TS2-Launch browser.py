# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter correct email address and password
# 7. Click 'login' button
# 8. Verify that 'Logged in as username' is visible
# 9. Click 'Delete Account' button
# 10. Verify that 'ACCOUNT DELETED!' is visible


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
else:
    print("Something goes wrong")
time.sleep(1)

#4. Click on 'Signup / Login' button

loginbutton = driver.find_element(By.XPATH,'//a[contains(@href,"/login")]') #We want go to login page
time.sleep(1)
loginbutton.click()

# 5. Verify 'Login to your account' is visible

logintab = driver.find_element(By.CLASS_NAME,'login-form')

if logintab.is_displayed():
    print('Login to your account is visible')
else:
    print('Try again')

# 6. Enter correct email address and password

def insertValue(inputname, inputvalue):                 #Definition that allows to fill the fields by faster way (email password.)
    nameofinput = (f"input[data-qa='{inputname}']")
    input = driver.find_element(By.CSS_SELECTOR,nameofinput)  
    input.send_keys(inputvalue)

insertValue('login-email','automationtester3@test.com')       #input e-mail adress e.g automationtester1@test.com
time.sleep(1)
insertValue('login-password','Tester1234')                     #input password e.g Tester1234
time.sleep(1)

# 7. Click 'login' button

loginbutton = driver.find_element(By.CSS_SELECTOR,'button[data-qa="login-button"')
loginbutton.click()
time.sleep(1)
# 8. Verify that 'Logged in as username' is visible

veryfiylog = driver.find_element(By.CSS_SELECTOR,'header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a')
if veryfiylog.is_displayed():
    print('Logged in as username is visible')
else:
    print('Try again!')

time.sleep(1)
# 9. Click 'Delete Account' button

deletebutton = driver.find_element(By.CSS_SELECTOR,'#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a').click()
time.sleep(7)
accdeleted = driver.find_element(By.CSS_SELECTOR,'#form > div > div > div > h2')

if accdeleted.is_displayed():
    print('ACCOUNT DELETED! is visible')
else:
    print('Trt again!')

time.sleep(5)
driver.quit()