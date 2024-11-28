import pytest
from selenium import webdriver

# Firefox webdriver
fDriver = webdriver.Firefox()


@pytest.fixture()
def setup():
    print('Start Setup')
    fDriver.get('https://www.ggeorgiou.gr/')

    yield  # commands executed after the main test
    print(' End Setup')
