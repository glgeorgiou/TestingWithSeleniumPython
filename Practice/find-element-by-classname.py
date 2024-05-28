"""
Selecting elements by using Class Name
- Combound classes are not allowed to use.
- Classes are repeated so, their usage is not suggested.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/login')

# fDriver.find_element(By.CLASS_NAME, "").send_keys('tomsmith')
# fDriver.find_element(By.CLASS_NAME, "").send_keys('SuperSecretPassword!')
fDriver.find_element(By.CLASS_NAME, 'radius').click()

# fDriver.quit()