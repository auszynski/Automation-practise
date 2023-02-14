def hide_ads(driver):
  print("Remove ads")
  driver.execute_script("[...document.querySelectorAll('.adsbygoogle')].map(el => el.parentNode.removeChild(el))")
  print("After remove ads")