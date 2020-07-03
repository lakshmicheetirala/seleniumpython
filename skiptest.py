import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_serach(self):
        print("This is serach test")

    def test_quickserach(self):
        print("This is Quicksreach test")

    @unittest.skip("This is not ready")
    def test_loginbygmail(self):
        print("This is Log in By Gmail Test")

    @unittest.skipIf(2 == 2, "Two equals two")
    def test_loginbytwiteer(self):
        print("This is log in bt Twitter")


if __name__ == "__main__":
    unittest.main()
