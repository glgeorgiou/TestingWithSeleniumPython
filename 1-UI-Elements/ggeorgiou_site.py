from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox webdriver for my cv site
fDriver = webdriver.Firefox()
fDriver.get('https://www.ggeorgiou.gr/')

"""
search posts that contain the word 'wordpress' and make an assertion
"""
# use css
# fDriver.find_element(By.ID, "s").send_keys('wordpress')
# fDriver.find_element(By.CSS_SELECTOR, ".searchsubmit").click()

# use xpath
fDriver.find_element(By.XPATH, "//input[@id='s']").send_keys('wordpress')
fDriver.find_element(By.XPATH, "//span[@class='ignition-icons ignition-icons-search']").click()

msg = fDriver.find_element(By.CLASS_NAME, "page-title").text
print(msg)
assert "21 results" in msg

"""
Click on a link
fDriver.find_element(By.LINK_TEXT, "GitHub – Online projects repository").click()
"""
