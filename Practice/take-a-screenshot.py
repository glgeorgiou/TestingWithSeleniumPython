"""
Visit the site and take a screenshot that is stored in current folder
"""
from selenium import webdriver

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/')

# Take the screenshot
fDriver.get_screenshot_as_file('the-internet-herokuapp-first-pge.png')