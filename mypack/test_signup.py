import pytest
import allure


@pytest.yield_fixture()
def setup():
    print("Open URL for signup")
    yield
    print("Close after signup")


@allure.description("this is my first python allure report")
def test_signupbyemail(setup):
    print("This is signup by email")


def test_signupbyfb(setup):
    print("This is Signup by fb")
