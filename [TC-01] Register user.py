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

#5. Verify 'New User Signup!' is visible

signUp = driver.find_element(By.CLASS_NAME,"signup-form")
if signUp.is_displayed():                    #We generate comunicate to verified that we are on login page accually
    print("New User Signup! is visible!")
else:
    print("Whoops! Try again")

#6. Enter name and email address

signNameTable = driver.find_element(By.CSS_SELECTOR,"input[data-qa='signup-name']") #Find "NAME" table by css_selector (data_qa)
signNameTable.send_keys('Tester12')        #input name in "name tab" e.g. Tester
time.sleep(1)
signEmail = signNameTable=driver.find_element(By.CSS_SELECTOR,"input[data-qa='signup-email']") #Find "signup email" table by css_selector (data_qa)
signEmail.send_keys('automationtester12@test.com') #input name in "email tab" e.g. automationtester@test.com

#7. Click 'Signup' button

signUpButton = driver.find_element(By.CSS_SELECTOR,"button[data-qa='signup-button']")  #Find signup button by css_selector (data_qa) and click that button
signUpButton.click()

#8. Verify that 'ENTER ACCOUNT INFORMATION' is visible

enterAcc = driver.find_element(By.CLASS_NAME,"login-form")  #We generate comunicate if we open the page of account information successfully or not
if enterAcc.is_displayed():
    print("'ENTER ACCOUNT INFORMATION' is visible!")
else:
    print("Ups! Somethings wrong!")

#9. Fill details: Title, Name, Email, Password, Date of birth

titleGender = driver.find_element(By.ID,"id_gender1")  #Find gender by id (Mr.-id_gender1  Mrs.-id_gender2)
titleGender.click()

registerPassword = driver.find_element(By.ID,"password")  #Enter the password e.g Tester123
registerPassword.send_keys("Tester1234") 

# registerdata = driver.find_element(By.ID,"days")      #Open days list
# registerdata.click()
# time.sleep(1)
# day = driver.find_element(By.CSS_SELECTOR,"option[value ='2']")  # select day (value = 1-31)
# day.click()
#for value in registerdata.find_element(By.TAG_NAME,'value'):
 #   if value.text == '6':
 #       value.click()

#registermonth = driver.find_element(By.ID,"months")
#registermonth.click()
#time.sleep(1)
#month = driver.find_element(By.CSS_SELECTOR,"option[value ='6']")  # select month 1-12 (1-January, 2-February 3-March ...)
#month.click()

#months = Select(driver.find_element_by_id('months'))
#months.select_by_value('5')


#registeryear = Select(driver.find_element_by_id('years'))
#registeryear.select_by_value('2002')

def selectValue(id, value):                         #Definition that allows to fill the fields wiht options to choose
    options = Select(driver.find_element(By.ID,id))   
    options.select_by_value(value)

selectValue('months', '5')
time.sleep(1)

selectValue('days', '10')
time.sleep(1)

selectValue('years', '2005')
time.sleep(1)

#10. Select checkbox 'Sign up for our newsletter!'

signUpNewsletter = driver.find_element(By.ID,'newsletter')
signUpNewsletter.click()
time.sleep(1)

#11. Select checkbox 'Receive special offers from our partners!'

recieveOffer = driver.find_element(By.ID,'optin')
recieveOffer.click()
time.sleep(1)

#12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number

# firstname = driver.find_element(By.CSS_SELECTOR,"input[data-qa='first_name']")  
# firstname.send_keys('John')

#lastname = driver.find_element(By.CSS_SELECTOR,"input[data-qa='last_name']")  
#lastname.send_keys('Smith')

def insertValue(inputname, inputvalue):                 #Definition that allows to fill the fields by faster way (Name, last name, address etc.)
    nameofinput = (f"input[data-qa='{inputname}']")
    input = driver.find_element(By.CSS_SELECTOR,nameofinput)  
    input.send_keys(inputvalue)

insertValue('first_name','John')
time.sleep(1)

insertValue('last_name','Smith')
time.sleep(1)

insertValue('company','CompanyIT')
time.sleep(1)

insertValue('address','Tester St. CompanyIT 11-000')
time.sleep(1)

insertValue('address2','Automation St. CompanyIT 11-000')
time.sleep(1)

selectValue('country','Canada')
time.sleep(1)

insertValue('state','Testing State')
time.sleep(1)

insertValue('city','Testing City')
time.sleep(1)

insertValue('zipcode','11-000')
time.sleep(1)

insertValue('mobile_number','100200300')
time.sleep(1)


#13. Click 'Create Account button'

createAccButton = driver.find_element(By.CSS_SELECTOR,"button[data-qa='create-account']") #Find and clck create account button
createAccButton.click()

#14. Verify that 'ACCOUNT CREATED!' is visible


accCreated = driver.find_element(By.CSS_SELECTOR,"h2[data-qa='account-created']")
if accCreated.is_displayed():
    print('ACCOUNT CREATED!')
else:
    print('Try again!')

time.sleep(1)

#15. Click 'Continue' button

continueButton = driver.find_element(By.CSS_SELECTOR,"a[data-qa='continue-button']")
continueButton.click()


#16. Verify that 'Logged in as username' is visible


deleteButton = driver.find_element(By.CSS_SELECTOR,'header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a > i') #Find delete account button

if deleteButton.is_displayed():
    print('Logged in as username! is visible')
else:
    print('Wrong!try again')

time.sleep(5)
#driver.refresh()
#time.sleep(7)

#17. Click 'Delete Account' button

deleteButton = driver.find_element(By.CSS_SELECTOR,'header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a > i').click()  #click delete account button
time.sleep(2)

#18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

accDeleted = driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div/h2')

if accDeleted.is_displayed():
    print('ACCOUNT DELETED! is visible')
else:
    print('Wrong!try again')

time.sleep(1)

cntbutton = driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div/div/a').click()

time.sleep(10)
driver.quit()