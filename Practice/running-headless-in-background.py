"""
# Run in headless mode - It supposed to run in the background but it doesn't
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Run in headless mode
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("Headless")  # Is it usefull?

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/abtest')

# Header 3 text and make assertion
headerText = fDriver.find_element(By.TAG_NAME, 'h3').text
print(f'The text of the header is: {headerText}')
assert  headerText == 'A/B Test Variation 1'