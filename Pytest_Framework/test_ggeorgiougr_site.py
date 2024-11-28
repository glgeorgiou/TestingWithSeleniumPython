"""
Using fixtures in plain way
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


def test_search_term__wordpress(setup):
    fDriver.find_element(By.XPATH, "//input[@id='s']").send_keys('wordpress')
    fDriver.find_element(By.XPATH, "//span[@class='ignition-icons ignition-icons-search']").click()


def test_search_term__seo(setup):
    fDriver.find_element(By.XPATH, "//input[@id='s']").send_keys('seo')
    fDriver.find_element(By.XPATH, "//span[@class='ignition-icons ignition-icons-search']").click()