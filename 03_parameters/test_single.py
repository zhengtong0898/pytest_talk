import pytest


@pytest.mark.parametrize(
    "test_input",
    ["a", "b", "c"]
)
def test_case_01(test_input):
    assert test_input in ("a", "b", "c")


@pytest.mark.parametrize(
    "test_input",
    [
        {"project_name": "pa01", "model_name": "po01"},
        {"project_name": "pa02", "model_name": "po02"},
        {"project_name": "pa03", "model_name": "po03"},
    ]
)
def test_case_02(test_input):
    assert test_input["project_name"] in ("pa01", "pa02", "pa03")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        ("2+4", 6),
        ("6*9", 54)
    ]
)
def test_case_03(test_input, expected):
    assert eval(test_input) == expected



