"""
Selecting elements by using name attribute
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/login')

fDriver.find_element(By.NAME, "username").send_keys('tomsmith')
fDriver.find_element(By.NAME, "password").send_keys('SuperSecretPassword!')
fDriver.find_element(By.CLASS_NAME, 'radius').click()

time.sleep(2)
# fDriver.quit()