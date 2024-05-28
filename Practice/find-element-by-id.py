"""
Selecting elements by using ID
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/login')

fDriver.find_element(By.ID, "username").send_keys('tomsmith')
fDriver.find_element(By.ID, "password").send_keys('SuperSecretPassword!')
fDriver.find_element(By.CLASS_NAME, 'radius').click()

# fDriver.quit()