import unittest


class Test(unittest.TestCase):
    def test_assertin(self):
        listv = {"python", "selenium", "java"}
        # self.assertIn("ruby", listv)
        self.assertNotIn("python", listv)


if __name__ == "__main__":
    unittest.main()
