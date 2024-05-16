"""
Implementing soon
"""
# Todo: mouse-interactions: comming soon
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

fDriver = webdriver.Firefox()

fDriver.maximize_window()
fDriver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Action Chain
action = ActionChains(fDriver)