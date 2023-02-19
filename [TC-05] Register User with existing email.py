# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'New User Signup!' is visible
# 6. Enter name and already registered email address
# 7. Click 'Signup' button
# 8. Verify error 'Email Address already exist!' is visible


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

#5. Verify 'New User Signup!' is visible

signup = driver.find_element(By.CLASS_NAME,"signup-form")
if signup.is_displayed():                    #We generate comunicate to verified that we are on login page accually
    print("New User Signup! is visible!")
else:
    print("Whoops! Try again")

# 6. Enter name and already registered email address

signnametable = driver.find_element(By.CSS_SELECTOR,"input[data-qa='signup-name']") #Find "NAME" table by css_selector (data_qa)
signnametable.send_keys('Tester7')        #input name in "name tab" e.g. Tester7 (already registered)
time.sleep(1)
signemail = signnametable=driver.find_element(By.CSS_SELECTOR,"input[data-qa='signup-email']") #Find "signup email" table by css_selector (data_qa)
signemail.send_keys('automationtester7@test.com') #input name in "email tab" e.g. automationtester7@test.com (already registered)

#7. Click 'Signup' button

signupbutton = driver.find_element(By.CSS_SELECTOR,"button[data-qa='signup-button']")  #Find signup button by css_selector (data_qa) and click that button
signupbutton.click()
time.sleep(1)

# 8. Verify error 'Email Address already exist!' is visible

alreadyexist = driver.find_element(By.CSS_SELECTOR,'#form > div > div > div:nth-child(3) > div > form > p')

if alreadyexist.is_displayed():
    print("'Email Address already exist!' is visible")

time.sleep(4)
driver.quit()