import unittest


class LoginTest(unittest.TestCase):
    def test_loginbyemail(self):
        print("Login by email Test")
        self.assertTrue(True)

    def test_loginbyfb(self):
        print("This is Login by facebook")
        self.assertTrue(True)

    def test_loginbytwitter(self):
        print("This is login by twitter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
