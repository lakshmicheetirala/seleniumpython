import pytest


@pytest.yield_fixture()
def setup():
    print("Once before every method")


def testMethod1(setup):
    print("This is test method1")


def testMethod2(teardown):
    print("This is test Method2")


@pytest.yield_fixture()
def teardown():
    yield
    print("This is after every method")
