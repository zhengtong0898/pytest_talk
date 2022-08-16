import unittest


class TestHello(unittest.TestCase):

    def test_case_01(self):
        self.assertTrue(True)

    @unittest.expectedFailure
    def test_case_02(self):
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_case_03(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
