import pytest


def test_SayHello():
    print('Hello there')


# @pytest.Mark.smoke # ToDo - Mark method does not have smoke and other attributes. Study pytest.
def test_bool():
    assert 4>3


def test_book2():
    assert -1<1