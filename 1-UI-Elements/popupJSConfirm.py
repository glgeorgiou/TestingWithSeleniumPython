from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/javascript_alerts')

fDriver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > button").click()

"""
# When click OK
popup = fDriver.switch_to.alert
# Switch to alert
popup.accept() # Click OK
# switch to driver
result = fDriver.find_element(By.ID, 'result').text

assert result == 'You clicked: Ok' # When clicked OK
"""


# When click cancel
popup = fDriver.switch_to.alert
# Switch to alert
popup.dismiss()    # Click Cancel
# switch to driver
result = fDriver.find_element(By.ID, 'result').text

assert  result == 'You clicked: Cancel'   # When clicked Cancel
