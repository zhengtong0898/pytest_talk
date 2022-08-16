import pytest


@pytest.fixture
def fixture01():
    print("Fixture01: before")
    yield
    print("Fixture01: after")


@pytest.fixture
def fixture02():
    print("Fixture02: before")
    yield
    print("Fixture02: after")


def test_case_01(fixture01, fixture02):
    print("running testcase")
    assert 1 == 1
