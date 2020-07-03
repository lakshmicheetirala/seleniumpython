# Relational comparision
# assertGreater
import unittest


class Test(unittest.TestCase):
    def testName(self):
        # self.assertGreater(100, 10)
        # self.assertGreaterEqual(100, 1000)
        self.assertLess(10, 100)
        self.assertLessEqual(1000, 100)


if __name__ == "__main__":
    unittest.main()
