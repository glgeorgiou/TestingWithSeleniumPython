"""
Switch between parent and child windows by using the-internet-heroku.com site
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for herokuapp site
fDriver = webdriver.Firefox()
fDriver.get('https://the-internet.herokuapp.com/windows')

fDriver.implicitly_wait(2)

fDriver.find_element(By.LINK_TEXT, 'Click Here').click()

# Return all the windows in a list format. window[0] is the parent.
windowsOpened = fDriver.window_handles
# Switch to the child window
fDriver.switch_to.window(windowsOpened[1])
print(fDriver.find_element(By.TAG_NAME, "h3").text)     # print the heading text

# Close current window, switch to parent window and make an assertion
fDriver.close()
fDriver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == fDriver.find_element(By.TAG_NAME, "h3").text