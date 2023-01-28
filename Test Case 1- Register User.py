from os import system
import time
from pkg_resources import find_distributions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() #browser which we choose
WebDriverWait(driver,10)
time.sleep(5)

driver.get('http://automationexercise.com') #website that we want to open
WebDriverWait(driver,5)
time.sleep(2) #test wait 3sec after open website
opensite = driver.find_element(By.ID,'header') #we want verified that the page opened successfully by view header part of home page
time.sleep(2) 
if opensite.is_displayed():                      #We generate comunicate if we open the page successfully or not
    print("The home page is visible successfully!") 
else:
    print("Something goes wrong")
time.sleep(2)
loginbutton = driver.find_element(By.XPATH,'//a[contains(@href,"/login")]') #We want go to login page
time.sleep(1)
loginbutton.click()
signemail=driver.find_element(By.NAME,"email")
if signemail.is_displayed():                    #We generate comunicate to verified that we are on login page accually (by find email table on login page)
    print("You are in login page!")
else:
    print("Whoops! Try again")
