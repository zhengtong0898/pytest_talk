import pytest


def test_case_01():
    assert True


@pytest.mark.xfail
def test_case_02():
    """
    xfail 跟常规的测试用例一样会被执行, 错误堆栈信息不会被打印出来.
    xfail 的测试用例, 失败了会被归纳到 xfailed 集合中.
    xfail 意味着失败用例是已知Bug导致, 符合预期.
    """
    assert False


@pytest.mark.xfail
def test_case_03():
    """
    xfail 的测试用例, 成功了会被归纳到 xpassed 集合中.
    xpassed 意味着Bug已经被修复了, 应该将当前标记去掉.
    """
    assert True
