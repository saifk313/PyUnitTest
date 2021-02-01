import unittest


class SkipTest(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search method")

    @unittest.skipIf(1 == 1, "Skipping Advanced Search")
    def test_advanced_search(self):
        print("This is advanced search method")

    @unittest.skipUnless(1 == 1, "Skipping Prepaid")
    def test_prepaid_search(self):
        print("This is prepaid search method")

    def test_postpaid_search(self):
        print("This is postpaid search method")


if __name__ == "__main__":
    unittest.main()
