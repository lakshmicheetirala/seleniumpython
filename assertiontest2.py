import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def test_name(self):
        driver = webdriver.Chrome(r"E:\selenium\drivers\chromedriver\chromedriver_83.exe")
        driver.get("https://www.google.com/")
        titleofpage = driver.title
        # self.assertTrue(titleofpage == "Google", "False if expression fails")
        self.assertFalse(titleofpage == "Google13")
