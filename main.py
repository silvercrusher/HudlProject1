import TestData.constant as const
import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait             # library is useful waiting for an element to load
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


os.environ['Path'] += r"C:/HudlProject1/driver"                     # environment path where the driver is located
driver = webdriver.Chrome()

driver.get(const.Base_url)                                             # HUDL home page url
driver.find_element(By.XPATH, "//a[normalize-space()='Log in']").click()    # hit Login button to enter credential

time.sleep(1)
print("1) Login Page: ", driver.title)                             # added extra layer for each navigation


#get need button element
need_button = driver.find_element(By.XPATH, "//a[normalize-space()='Need help?']")
need_button.click()

login_help_page_url = "https://www.hudl.com/login/help"
#assert(driver.current_url = login_help_page_url)



# sign up button functionality from login/help page
sign_up = driver.find_element(By.XPATH, "//a[normalize-space()='Sign up']")
webdriver.ActionChains(driver).double_click(sign_up)
driver.back()
time.sleep(2)


# hitting back button from login/help page to navigate back
back_help = driver.find_element(By.XPATH, "//a[@class='styles_backIconContainer_MhkioW9m8rx70X7CIGuws']")
#back_help.click()

# double clicking the back button
webdriver.ActionChains(driver).double_click(back_help).perform()

time.sleep(2)
#need to create a loading scenario

email = driver.find_element(By.XPATH, "//input[@id='email']")
password = driver.find_element(By.XPATH, "//input[@id='password']")

# insert credentials using the relative xpath

###############   negative scenario, hitting enter without entering pwd  ##################
email.send_keys(const.email, Keys.ENTER)
time.sleep(2)

###############   negative scenario, entering negative credential  ##################33
email.clear()
email.send_keys(const.email)
driver.implicitly_wait(500)
password.send_keys("Aminul012", Keys.ENTER)
time.sleep(2)

###############   positive scenario   ##################33
# insert credentials using the relative xpath
email.clear()
email.send_keys(const.email)
driver.implicitly_wait(500)
password.clear()
password.send_keys(const.password)

# instead of hitting the Login button, we can trigger keyboard Enter button
# driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Aminul0123" + Keys.ENTER)


time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='logIn']").click()


driver.maximize_window()
time.sleep(5)           # wanted the process to wait some time before it moves to the profile page
print("2) Profile Page: ", driver.title)
print(driver.current_url)

driver.find_element(By.XPATH, "//span[normalize-space()='Coach I']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Your Profile']")

driver.quit()

