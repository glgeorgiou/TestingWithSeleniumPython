from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

# Firefox webdriver for herokuapp site
fDriverHA = webdriver.Firefox()
fDriverHA.get('https://the-internet.herokuapp.com/')

# Click on drop down link
fDriverHA.find_element(By.CSS_SELECTOR, "a[href='/dropdown']").click()

# Drop down list and select items
dropdown = Select(fDriverHA.find_element(By.ID, "dropdown"))
# Select option 1
dropdown.select_by_index(1)
# Select option 2
dropdown.select_by_index(2)
# NOTE: Complete testing code at https://elementalselenium.com/tips/5-select-from-a-dropdown