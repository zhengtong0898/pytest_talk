import unittest


class TestHello(unittest.TestCase):

    def setUp(self) -> None:
        print("do something before run testcase")

    def test_case(self):
        print("running testcase")
        self.assertEqual(1, 1)

    def tearDown(self) -> None:
        print("do something after run testcase")


if __name__ == '__main__':
    unittest.main()
