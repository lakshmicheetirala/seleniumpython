import unittest
from selenium import webdriver


class SearchTitle(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver_83.exe")
        driver.get("https://www.google.com/")
        title = driver.title
        # self.assertEqual("Google1", title, "Web page titles are not matched")
        self.assertNotEqual("Google1", title, "Web page titles are not matched")


# if __name__ == "__main__":
#     unittest.main()