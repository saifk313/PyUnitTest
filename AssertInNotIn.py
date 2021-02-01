import unittest


class AssertInNotIn(unittest.TestCase):

    def testInNotIn(self):
        my_list = {"python", "java", "ruby", "pearl", "c#"}
        self.assertIn("python", my_list)
        self.assertNotIn("xz", my_list)


if __name__ == "__main__":
    unittest.main()
