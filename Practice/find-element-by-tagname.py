"""
Selecting elements by using Tag Name.
Case when there are more than one html elements with the same name.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/')

# Goto tables page
fDriver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()

# Select all rows from the first table -
# ToDo: Future development
table = fDriver.find_element(By.ID, 'table1')

# time.sleep(2)
# fDriver.quit()