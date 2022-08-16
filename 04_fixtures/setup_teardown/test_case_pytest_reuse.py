import pytest


@pytest.fixture
def setup_project():
    print("do something before run testcase")
    yield
    print("do something after run testcase")


def test_case_01(setup_project):
    print("running testcase")
    assert 1 == 1


def test_case_02(setup_project):
    print("running testcase")
    assert 1 == 1
