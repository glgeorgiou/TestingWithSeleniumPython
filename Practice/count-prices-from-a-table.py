from selenium import webdriver
from selenium.webdriver.common.by import By

veggiesPrices = []  # a list for storied values
sumOfVeggies = 0

# Firefox webdriver for site
fDriver = webdriver.Firefox()
fDriver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')

# collect all veggie prices
veggieWebElements = fDriver.find_elements(By.XPATH, "//tr/td[2]")
for ele in veggieWebElements:
    veggiesPrices.append(int(ele.text))

# sum of veggie's prices
for ele in veggiesPrices:
    sumOfVeggies += ele

print('List of prices is:',veggiesPrices)
print('The sum of prices is:', sumOfVeggies)

# Future assert comparing the sum with a totel displayed value