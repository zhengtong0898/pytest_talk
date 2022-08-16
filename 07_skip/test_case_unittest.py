import sys
import unittest


class TestHello(unittest.TestCase):

    def test_case_01(self):
        self.assertTrue(True)

    @unittest.skip
    def test_case_02(self):
        self.assertTrue(True)

    def test_case_03(self):
        self.assertTrue(True)

    @unittest.skipIf(sys.platform == "darwin", reason="skip on darwin")
    def test_case_04(self):
        assert True


if __name__ == '__main__':
    unittest.main()
