import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def test_Name(self):
        driver = None
        driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver_83.exe")
        # self.assertIsNone(driver)
        self.assertIsNotNone(driver)
