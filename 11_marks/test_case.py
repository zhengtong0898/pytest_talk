import pytest


@pytest.mark.p1
def test_case_01():
    assert True


@pytest.mark.p1
@pytest.mark.slow
@pytest.mark.unstable
def test_case_02():
    assert True


@pytest.mark.p2
def test_case_03():
    assert True


@pytest.mark.p3
def test_case_04():
    assert True


@pytest.mark.slow
def test_case_05():
    assert True


@pytest.mark.unstable
def test_case_06():
    assert True
