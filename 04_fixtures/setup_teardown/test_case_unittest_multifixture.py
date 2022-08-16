import unittest


class Fixture01(unittest.TestCase):

    def setUp(self) -> None:
        print("Fixture01: before")

    def tearDown(self) -> None:
        print("Fixture01: after")


class Fixture02(Fixture01):

    def setUp(self) -> None:
        super(Fixture02, self).setUp()
        print("Fixture02: before")

    def tearDown(self) -> None:
        print("Fixture02: after")
        super(Fixture02, self).tearDown()


class TestHello(Fixture02):

    def test_case_01(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
