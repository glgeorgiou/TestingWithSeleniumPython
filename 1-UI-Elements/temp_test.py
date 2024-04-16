from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://rahulshettyacademy.com/AutomationPractice/')

# RADIO BUTTONS - Check if 2nd is clicked
radiobuttons = fDriver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected() #Make sure that 3rd radio button is selected