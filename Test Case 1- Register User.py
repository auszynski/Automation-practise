#1. Launch browser
#2. Navigate to url 'http://automationexercise.com'
#3. Verify that home page is visible successfully
#4. Click on 'Signup / Login' button
#5. Verify 'New User Signup!' is visible
#6. Enter name and email address
#7. Click 'Signup' button
#8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
#9. Fill details: Title, Name, Email, Password, Date of birth
#10. Select checkbox 'Sign up for our newsletter!'
#11. Select checkbox 'Receive special offers from our partners!'
#12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
#13. Click 'Create Account button'
#14. Verify that 'ACCOUNT CREATED!' is visible
#15. Click 'Continue' button
#16. Verify that 'Logged in as username' is visible
#17. Click 'Delete Account' button
#18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button


from os import system
import time
from pkg_resources import find_distributions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

#1. Launch browser

driver = webdriver.Chrome() #browser which we choose
WebDriverWait(driver,10)
time.sleep(5)

#2. Navigate to url 'http://automationexercise.com'

driver.get('http://automationexercise.com') #website that we want to open
WebDriverWait(driver,5)
time.sleep(2) #test wait 3sec after open website

#3. Verify that home page is visible successfully


opensite = driver.find_element(By.ID,'header') #we want verified that the page opened successfully by view header part of home page
time.sleep(2) 
if opensite.is_displayed():                      #We generate comunicate if we open the page successfully or not
    print("The home page is visible successfully!") 
else:
    print("Something goes wrong")
time.sleep(2)

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

#6. Enter name and email address

signnametable = driver.find_element(By.CSS_SELECTOR,"input[data-qa='signup-name']") #Find "NAME" table by css_selector (data_qa)
signnametable.send_keys('Tester')        #input name in "name tab" e.g. Tester
time.sleep(1)
signemail = signnametable=driver.find_element(By.CSS_SELECTOR,"input[data-qa='signup-email']") #Find "signup email" table by css_selector (data_qa)
signemail.send_keys('automationtester@test.com') #input name in "email tab" e.g. automationtester@test.com

#7. Click 'Signup' button

signupbutton = driver.find_element(By.CSS_SELECTOR,"button[data-qa='signup-button']")  #Find signup button by css_selector (data_qa) and click that button
signupbutton.click()

#8. Verify that 'ENTER ACCOUNT INFORMATION' is visible

enteracc = driver.find_element(By.CLASS_NAME,"login-form")  #We generate comunicate if we open the page of account information successfully or not
if enteracc.is_displayed():
    print("'ENTER ACCOUNT INFORMATION' is visible!")
else:
    print("Ups! Somethings wrong!")

#9. Fill details: Title, Name, Email, Password, Date of birth

titlegender = driver.find_element(By.ID,"id_gender1")  #Find gender by id (Mr.-id_gender1  Mrs.-id_gender2)
titlegender.click()

registerpassword = driver.find_element(By.ID,"password)  #Enter the password e.g Tester123
registerpassword.send_keys("Tester123") 

registerdata = driver.find_element(By.CLASS_NAME,"days")
registerdata.click()
for option in registerdata.find_element(By.TAG_NAME,'option'):
    if option.text == '6':
        option.click()

#registermonth = driver.find_element(By.CLASS_NAME,"months")


#registeryear = driver.find_element(By.CLASS_NAME,"years")