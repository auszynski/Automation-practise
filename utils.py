from selenium.webdriver.common.by import By

def hide_ads(driver):
  print("Remove ads")
  driver.execute_script("[...document.querySelectorAll('.adsbygoogle')].map(el => el.parentNode.removeChild(el))")
  print("After remove ads")
  print("First click to fire ads")
  tc = driver.find_element(By.CSS_SELECTOR,'#header > div > div > div > div.col-sm-4 > div > a > img')
  tc.click()