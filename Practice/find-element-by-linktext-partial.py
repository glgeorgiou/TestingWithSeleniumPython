"""
Selecting elements by using Partial Link Text (in case of long link names).
Link names must be unique in order to use the PARTIAL_LINK_TEXT option.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com')

# Goto  JavaScript onload event error link
fDriver.find_element(By.PARTIAL_LINK_TEXT, 'JavaScript onload').click()

# time.sleep(2)
# fDriver.quit()