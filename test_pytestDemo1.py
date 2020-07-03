import pytest


@pytest.fixture()
def setup():
    print("Once before every method")


def testMethod1(setup):
    print("this is Test Method1")


def testMethod2():
    print("This is Test Method2")
