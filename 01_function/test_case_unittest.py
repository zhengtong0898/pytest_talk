import unittest


class TestHello(unittest.TestCase):

    def test_case(self):
        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()
