import pytest

'''
#Simple fixture
@pytest.fixture()
def setup():
    print('I will be executed first')
    yield
    print('I will executed last')

def test_fixtureDemo(setup):
    print('I will execute steps in fixture method')
'''



@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("i will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo3 method")