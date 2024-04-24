import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver
fDriver = webdriver.Firefox()

# wait until 5 seconds if object is not displayed
# 1.5 second to reach next page- execution will resume in 1.5 seconds
# if object do not show up at all, then max time your test waits for 5 seconds
fDriver.implicitly_wait(5)

# Driver
fDriver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

# Get and count elements
fDriver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys('ber')
time.sleep(4)
count = len(fDriver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert  count == 3

# Add elements to the cart
buttons = fDriver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in buttons:
    button.click()

    # NOTE: Site https://wp-eshop.ggeorgiou.work/, products= (hoodie)
