from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/javascript_alerts')

fDriver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(1) > button").click()

# Switch to alert
popup = fDriver.switch_to.alert
popup.accept()
# switch to driver
result = fDriver.find_element(By.ID, 'result').text

assert result == 'You successfully clicked an alert'



