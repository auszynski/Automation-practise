from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def hide_ads(driver):
  print("Remove ads")
  driver.execute_script("[...document.querySelectorAll('.adsbygoogle')].map(el => el.parentNode.removeChild(el))")
  print("After remove ads")
  print("First click to fire ads!")
  tc = driver.find_element(By.CSS_SELECTOR,'#header > div > div > div > div.col-sm-4 > div > a > img')
  tc.click()


def openSiteProcess():
  print('Testing process start')
  driver = webdriver.Chrome()
  WebDriverWait(driver,10)
  time.sleep(1)

  driver.get('http://automationexercise.com')
  WebDriverWait(driver,1)
  time.sleep(1) 

  opensite = driver.find_element(By.ID,'header')
  time.sleep(1) 
  if opensite.is_displayed():
    print("The home page is visible successfully!") 