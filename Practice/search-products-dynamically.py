"""
Go to the https://wp-eshop.ggeorgiou.work/ test e-shop,
search a product in a dynamic search field,
view all results
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver
fDriver = webdriver.Firefox()
fDriver.get('https://wp-eshop.ggeorgiou.work/shop/')

fDriver.implicitly_wait(5)

# search term
fDriver.find_element(By.XPATH, "(//input[@name='s'])[1]").send_keys('hoodie')

# view all results - BUG: The operation is broken.
# The 'view results' link is not visible and you have to scroll the results window
fDriver.find_element(By.CSS_SELECTOR, "aws_result_item aws_search_more").click()
