"""
Using fixtures by using class
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

fDriver = webdriver.Firefox()

"""
@pytest.fixture()
def setup():
    print('Start Setup')
    # Firefox webdriver
    fDriver.get('https://www.ggeorgiou.gr/')

    yield  # commands executed after the main test
    print(' End Setup') 
"""


@pytest.mark.usefixtures("setup")
class Test_GG_Site:

    def test_search_term__html(self):
        fDriver.find_element(By.XPATH, "//input[@id='s']").send_keys('html')
        fDriver.find_element(By.XPATH, "//span[@class='ignition-icons ignition-icons-search']").click()

    def test_search_term__css(self):
        fDriver.find_element(By.XPATH, "//input[@id='s']").send_keys('css')
        fDriver.find_element(By.XPATH, "//span[@class='ignition-icons ignition-icons-search']").click()