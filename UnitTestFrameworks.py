import unittest


# Execution Flow:
# setUpModule -> setUpClass -> setUp -> classMethods -> tearDown -> tearDownClass -> tearDownModule

def setUpModule():
    print('Open Browser')


def tearDownModule():
    print("Close Browser")


class UnitTestFramework(unittest.TestCase):

    @classmethod
    def setUp(cls):
        print('This is login test')

    @classmethod
    def tearDown(cls):
        print("This is logout test \n")

    @classmethod
    def setUpClass(cls):
        print('Open application \n')

    @classmethod
    def tearDownClass(cls):
        print("Close Application")

    def test_search(self):
        print("This is search method")

    def test_advanced_search(self):
        print("This is advanced search")

    def test_prepaid_reacharge(self):
        print("This is prepaid")

    def test_pospaid_recharge(self):
        print("This is postpaid")


if __name__ == "__main__":
    unittest.main()
