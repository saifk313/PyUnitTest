import unittest


class RelationAssertion(unittest.TestCase):

    def test_relations(self):
        self.assertGreater(100, 1, "100 > 1")
        self.assertGreaterEqual(100, 100, "100 = 100")
        print("Assert")
        # self.assertLess(100, 1, "100 < 1")
        # self.assertLessEqual(100, 1, "100 != 1")


if __name__ == "__main__":
    unittest.main()
