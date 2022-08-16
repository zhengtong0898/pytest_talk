import pytest


@pytest.fixture
def setup_project():
    print("do something before run testcase")
    yield
    print("do something after run testcase")


def test_case(setup_project):
    print("running testcase")
    assert 1 == 1
