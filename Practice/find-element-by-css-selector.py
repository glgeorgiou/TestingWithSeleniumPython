"""
Selecting elements by using CSS selector
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/login')

fDriver.find_element(By.CSS_SELECTOR, "#username").send_keys('tomsmith')
fDriver.find_element(By.CSS_SELECTOR, "[type=password]").send_keys('SuperSecretPassword!')
fDriver.find_element(By.CSS_SELECTOR, '.radius').click()

# fDriver.quit()