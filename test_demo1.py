# Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
import pytest

def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

#Pass as parameter the 'crossBrowser' method from conftest.py file.
def test_crossBrowser(crossBrowser):
    print(crossBrowser[0]) #Ο δείκτης 1
    print(crossBrowser[1])  #με την σειρά οι δείκτες 0,1,2
    print(crossBrowser[2])  
