import unittest


class TestHello(unittest.TestCase):

    def test_case(self):
        self.assertEqual(1, 1)
        self.assertNotEqual("a", "b")
        self.assertTrue("a" == "a")
        self.assertFalse("a" == "b")
        self.assertIs(True, True)
        self.assertIsNot(True, False)
        self.assertIsNone(None)
        self.assertIsNotNone("x")
        self.assertIn("a", ("a", "b", "c"))
        self.assertNotIn("a", ("b", "c", "d"))
        self.assertIsInstance("a", str)
        self.assertNotIsInstance(1, str)

        self.assertGreater(1, 0)
        self.assertGreaterEqual(1, 1)
        self.assertLess(1, 2)
        self.assertLessEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
