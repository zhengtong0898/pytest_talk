import pytest


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
