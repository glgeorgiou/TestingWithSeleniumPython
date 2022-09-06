
import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_firstProgram():
    msg = "Hello"  # operations
    assert msg == "Hi", "Test failed because strings do not match"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"


@pytest.fixture()
def setup():
    print('I will be executed first')
def test_fixtureDemo(setup):
    print('I will execute steps in fixture method')
