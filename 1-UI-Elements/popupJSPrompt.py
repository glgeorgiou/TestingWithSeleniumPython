from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/javascript_alerts')

fDriver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(3) > button").click()

promptedName = 'George'

# Switch to alert
popup = fDriver.switch_to.alert
popup.send_keys(promptedName)
alertText = popup.text
popup.accept()

# switch to driver
print('Name = ',promptedName)
result = fDriver.find_element(By.ID, 'result').text
assert result == 'You entered: '+promptedName