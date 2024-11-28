import pytest
from selenium import webdriver

@pytest.fixture(scope="class")  # Χρησιμοποιούμε το scope "class" για να χρησιμοποιείται εντός class
def setup(request):  # Εδώ διαχειριζόμαστε το driver
    print('Start Setup')
    driver = webdriver.Firefox()
    driver.get('https://www.ggeorgiou.gr/')

    # Μοιράζουμε τον driver στα tests
    request.cls.driver = driver

    yield driver

    print('End Setup')
    driver.quit()