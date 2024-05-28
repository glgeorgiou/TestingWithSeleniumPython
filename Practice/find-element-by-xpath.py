"""
Selecting elements by using XPath
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for Google site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/login')

fDriver.find_element(By.XPATH, "//input[@type='text']").send_keys('tomsmith')
fDriver.find_element(By.XPATH, "//input[@type='password']").send_keys('SuperSecretPassword!')
fDriver.find_element(By.XPATH, "//button[@type='submit']").click()

# fDriver.quit()