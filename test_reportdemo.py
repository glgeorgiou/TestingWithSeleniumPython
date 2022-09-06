def test_screenshot_on_test_failure(browser):
    # driver = webdriver.Firefox()
    browser.get("https://microsoft.com")
    assert 2 == 4-2