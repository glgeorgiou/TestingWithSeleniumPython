"""
Using fixtures by using class
"""
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")  # Fixture name "setu" will be used from the class.
class Test_GG_Site:

    def test_search_term__wordpress(self):
        self.driver.find_element(By.XPATH, "//input[@id='s']").send_keys('wordpress')
        self.driver.find_element(By.XPATH, "//span[@class='ignition-icons ignition-icons-search']").click()

    def test_search_term__seo(self):
        self.driver.find_element(By.XPATH, "//input[@id='s']").send_keys('seo')
        self.driver.find_element(By.XPATH, "//span[@class='ignition-icons ignition-icons-search']").click()
