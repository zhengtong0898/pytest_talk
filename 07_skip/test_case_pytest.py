import sys
import pytest


def test_case_01():
    assert True


@pytest.mark.skip
def test_case_02():
    assert True


def test_case_03():
    assert True


@pytest.mark.skipif(sys.platform == "darwin", reason="skip on darwin")
def test_case_04():
    assert True
