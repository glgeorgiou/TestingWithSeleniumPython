from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for herokuapp site
fDriverHA = webdriver.Firefox()
fDriverHA.get('https://the-internet.herokuapp.com/')

# Click on checkboxes link
fDriverHA.find_element(By.CSS_SELECTOR, "a[href='/checkboxes']").click()

# CHECKBOXES - check if 2nd checkbox is selected
# # How many checkboxes do we have
checkboxes = fDriverHA.find_elements(By.XPATH, "//input[@type='checkbox']")
print("There are {} checkboxes".format(len(checkboxes)))

# Check if first checkbox is clicked
checkboxes[0].click()
for cBox in checkboxes:
    assert cBox.is_selected()
    break
