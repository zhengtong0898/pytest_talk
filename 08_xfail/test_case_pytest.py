import pytest


def test_case_01():
    assert True


@pytest.mark.xfail
def test_case_02():
    assert False
