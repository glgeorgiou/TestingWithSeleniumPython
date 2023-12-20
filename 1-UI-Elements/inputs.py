from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for herokuapp site
fDriverHA = webdriver.Firefox()
"""
fDriverHA.get('https://the-internet.herokuapp.com/')

# Click on inputs link
fDriverHA.find_element(By.CSS_SELECTOR, "a[href='/inputs']").click()
# fDriverHA.find_element((By.CSS_SELECTOR, "input[type='number']")).send_keys(7) # TODO: Error message in internal file

"""

# Enter values in https://rahulshettyacademy.com/angularpractice/