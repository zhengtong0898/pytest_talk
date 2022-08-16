import pytest


# parameter的加载和执行顺序是: LIFO，所以会先执行最下面的parameters然后再执行最上面的parameters
@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
@pytest.mark.parametrize("other_input", ["linux", "python", "pytest"])
def test_eval(other_input, test_input, expected):
    assert eval(test_input) == expected
