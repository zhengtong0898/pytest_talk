import unittest


def aa(variable_a) -> None:
    variable_b = {"hello": "world"}
    variable_c = ("godw", "pppp")
    bb(variable_b, variable_c)


def bb(vb, vc) -> None:
   cc(vc)


def cc(final):
    assert final == 1


class TestHello(unittest.TestCase):

    def test_case(self):
        count = 10
        aa(count)


if __name__ == '__main__':
    unittest.main()
