import unittest


class Fixture(unittest.TestCase):

    def setUp(self) -> None:
        print("do something before run testcase")

    def tearDown(self) -> None:
        print("do something after run testcase")


class TestHello(Fixture):

    def test_case_01(self):
        self.assertEqual(1, 1)

    def test_case_02(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
