"""
Using fixtures by using class
"""
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")  # Fixture name "setu" will be used from the class.
class Test_GG_Site2:

    def test_search_term__html(self):
        self.driver.find_element(By.XPATH, "//input[@id='s']").send_keys('html')
        self.driver.find_element(By.XPATH, "//span[@class='ignition-icons ignition-icons-search']").click()

    def test_search_term__css(self):
        self.driver.find_element(By.XPATH, "//input[@id='s']").send_keys('css')
        self.driver.find_element(By.XPATH, "//span[@class='ignition-icons ignition-icons-search']").click()
