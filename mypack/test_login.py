import pytest


@pytest.yield_fixture()
def setup():
    print("Open URL to login")
    yield
    print("Closing after login")


def test_loginbyemail(setup):
    print("This is Login by email")


def test_loginbyfb(setup):
    print("This is login by Facebook")
