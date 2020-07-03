import unittest


def setUpModule():  # This will be excuted before any class or method prasent in the unittest class
    print("setUpModule")


def tearDownModule():  # This will be excuted after any class or method prasent in the unittest class
    print("tearDownModule")


class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):  # execute before all test methods
        print("This is setup")

    def test_serach(self):  # execute after all test methods
        print("This is start serach")

    def test_advancedserach(self):
        print("This is Advanced Serach")

    @classmethod
    def setUpClass(cls):  # execute once when the class started
        print("Open Application")

    @classmethod
    def tearDownClass(cls):  # execute once after the class completed
        print("close Application")

    @classmethod
    def tearDown(self):
        print("This is teardown")


if __name__ == "__main__":
    unittest.main()
