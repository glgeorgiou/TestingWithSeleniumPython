"""
Find the 'Mouse Hover' button and click on the 'Top' option.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

fDriver = webdriver.Firefox()

fDriver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Find the Mouse Hover button
mouse_hover_button = fDriver.find_element(By.ID, "mousehover")

# Scroll the window to the Mouse Hover button
fDriver.execute_script("arguments[0].scrollIntoView();", mouse_hover_button)

# Create an action chain object
actions = ActionChains(fDriver)

# Move to the Mouse Hover button to display the hidden menu
actions.move_to_element(mouse_hover_button).perform()

# Wait for the menu to appear
time.sleep(2)

# Find the Top menu option
top_option = fDriver.find_element(By.LINK_TEXT, "Top")

# Click on the Top menu option
top_option.click()

# Wait for a few seconds to see the result
time.sleep(5)