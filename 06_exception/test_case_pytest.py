

def aa(variable_a) -> None:
    variable_b = {"hello": "world"}
    variable_c = ("godw", "pppp")
    bb(variable_b, variable_c)


def bb(vb, vc) -> None:
   cc(vc)


def cc(final):
    assert final == 1


def test_case() -> None:
    count = 10
    aa(count)
