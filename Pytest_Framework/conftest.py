import pytest
from selenium import webdriver

@pytest.fixture(scope="class")  # Use the "class" scope for usage into a class
def setup(request):  # We operate driver
    print('Start Setup')
    driver = webdriver.Firefox()
    driver.get('https://www.ggeorgiou.gr/')

    # Sharing driver in tests
    request.cls.driver = driver

    yield driver

    print('End Setup')
    driver.quit()