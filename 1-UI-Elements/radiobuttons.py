from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://rahulshettyacademy.com/AutomationPractice/')

# RADIO BUTTONS - Check if all radio buttons are clicked
radioButtons = fDriver.find_elements(By.CSS_SELECTOR, ".radioButton")
for rd in radioButtons:
    rd.click()
    assert rd.is_selected()