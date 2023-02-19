# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter incorrect email address and password
# 7. Click 'login' button
# 8. Verify error 'Your email or password is incorrect!' is visible

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


openSite = driver.find_element(By.ID,'header') #we want verified that the page opened successfully by view header part of home page
time.sleep(1) 
if openSite.is_displayed():                      #We generate comunicate if we open the page successfully or not
    print("The home page is visible successfully!") 
else:
    print("Something goes wrong")
time.sleep(1)

#4. Click on 'Signup / Login' button

loginButton = driver.find_element(By.XPATH,'//a[contains(@href,"/login")]') #We want go to login page
time.sleep(1)
loginButton.click()

# 5. Verify 'Login to your account' is visible

loginTab = driver.find_element(By.CLASS_NAME,'login-form')

if loginTab.is_displayed():
    print('Login to your account is visible')
else:
    print('Try again')

# 6. Enter incorrect email address and password

def insertValue(inputname, inputvalue):                 #Definition that allows to fill the fields by faster way (email password.)
    nameofinput = (f"input[data-qa='{inputname}']")
    input = driver.find_element(By.CSS_SELECTOR,nameofinput)  
    input.send_keys(inputvalue)

insertValue('login-email','automationtester100@test.com')       #input incorrect e-mail adress e.g automationtester100@test.com
time.sleep(1)
insertValue('login-password','Tester12345')                     #input incorrect password e.g Tester12345
time.sleep(1)

# 7. Click 'login' button

loginButton = driver.find_element(By.CSS_SELECTOR,'button[data-qa="login-button"')
loginButton.click()
time.sleep(1)

# 8. Verify error 'Your email or password is incorrect!' is visible

incorrectValues = driver.find_element(By.CSS_SELECTOR,'#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > p')
if incorrectValues.is_displayed():
    print('Your email or password is incorrect! is visible')
else:
    print('Try again!')

time.sleep(2)
driver.quit()