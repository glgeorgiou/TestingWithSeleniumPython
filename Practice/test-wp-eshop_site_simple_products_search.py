from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for my cv site
fDriver = webdriver.Firefox()
fDriver.get('https://wp-eshop.ggeorgiou.work/shop/')

# Search for 'beanie' products
fDriver.find_element(By.ID, "wp-block-search__input-1").send_keys('beanie')
fDriver.find_element(By.XPATH, "//button[@aria-label='Αναζήτηση']").click()

# Add products into cart
results = fDriver.find_elements(By.CSS_SELECTOR, "ul > li")
countProducts = len(results)
assert countProducts > 0
for product in results:
    fDriver.find_element(By.CSS_SELECTOR, "li button").click()
    # ToDo: wp-eshop-1. Need scroll down action

# Todo: 2. wp-eshop-2 - Goto cart and check if the sum is valid - file: ExplicitwaitDemo1.
