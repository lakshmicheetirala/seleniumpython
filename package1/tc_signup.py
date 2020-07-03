import unittest


class SignupTest(unittest.TestCase):
    def test_signupbyemail(self):
        print("Signup by email Test")
        self.assertTrue(True)

    def test_signupbyfb(self):
        print("This is Signup by facebook")
        self.assertTrue(True)

    def test_signupbytwitter(self):
        print("This is Signup by twitter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
