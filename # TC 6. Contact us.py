# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Contact Us' button
# 5. Verify 'GET IN TOUCH' is visible
# 6. Enter name, email, subject and message
# 7. Upload file
# 8. Click 'Submit' button
# 9. Click OK button
# 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
# 11. Click 'Home' button and verify that landed to home page successfully


from operator import imod
from os import system
import time
from pkg_resources import find_distributions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

import pyautogui
from selenium.webdriver.chrome.options import Options

#option1 = Options()
#option1.add_argument("--disable-notification")

#1. Launch browser

driver = webdriver.Chrome() #(chrome_options= option1) #browser which we choose
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

# 4. Click on 'Contact Us' button

contact = driver.find_element(By.CSS_SELECTOR,'#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(8) > a').click()

time.sleep(1)

# 5. Verify 'GET IN TOUCH' is visible
getin = driver.find_element(By.CSS_SELECTOR,'#contact-page > div.row > div.col-sm-8 > div > h2')

if getin.is_displayed():
    print('"GET IN TOUCH" is visible')

time.sleep(1)

# 6. Enter name, email, subject and message

def insertValue(inputname, inputvalue):                 #Definition that allows to fill the fields by faster way (name,email,subject, your message.)
    nameofinput = (f"input[data-qa='{inputname}']")
    input = driver.find_element(By.CSS_SELECTOR,nameofinput)  
    input.send_keys(inputvalue)

insertValue('name','Tester1')      
time.sleep(1)
insertValue('email','automationtester1@test.com')               
time.sleep(1)
insertValue('subject','Return of products')
time.sleep(1)
#insertValue('message','I want to return the pair of black pants. Can you help me?')

mesage = driver.find_element(By.CSS_SELECTOR,'#message')
mesage.send_keys('I want to return the pair of black pants. Can you help me?')
time.sleep(2)

# 7. Upload file

#first try with method from stackoverflow
# uploadfile = driver.find_element(By.CSS_SELECTOR,'#contact-us-form > div:nth-child(6)').send_keys("/Users/Artur/Pictures/pants.jpeg")

# uploadfile.send_keys('/Users/Artur/Pictures/1665678985220-kopia.jpeg')
# time.sleep(15)

# element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="contact-us-form"]/div[5]/input'))  # Example xpath
# time.sleep(2)

#UPLOAD FILE BY PYAUTOGUI
wybierz = driver.find_element(By.CSS_SELECTOR,'#contact-us-form >div:nth-child(6)').click()
time.sleep(3)

WebDriverWait(driver,10)
pyautogui.write('/users/artur/obrazki/pants.jpeg', interval=0.40) 
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')

# 8. Click 'Submit' button

submit = driver.find_element(By.CSS_SELECTOR,'#contact-us-form > div:nth-child(7) > input').click()

time.sleep(4)

# 9. Click OK button
WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()

# 10. Verify success message 'Success! Your details have been submitted successfully.' is visible

success = driver.find_element(By.CSS_SELECTOR,'#contact-page > div.row > div.col-sm-8 > div > div.status.alert.alert-success')

if success.is_displayed():
    print("'Success! Your details have been submitted successfully.' is visible")

time.sleep(1)

# 11. Click 'Home' button and verify that landed to home page successfully

home = driver.find_element(By.CSS_SELECTOR,'#form-section > a').click()

time.sleep(4)

homepage = driver.find_element(By.CSS_SELECTOR,'body > section:nth-child(3) > div > div > div.col-sm-3 > div > h2')

if homepage.is_displayed():
    print('Welcome on home page')

time.sleep(3)
driver.quit()