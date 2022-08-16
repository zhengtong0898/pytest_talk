import pytest


# 当已知某个参数是受限是，通过pytest.param方法可以标记跳过该参数的测试。
@pytest.mark.parametrize(
    "platform",
    [
        "windows",
        "linux",
        pytest.param("darwin", marks=pytest.mark.skip),
    ]
)
def test_case_04(platform):
    assert platform in ("windows", "linux")
