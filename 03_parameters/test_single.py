import pytest


# 在没有parameters功能之前, 对于多个参数多种组合测试场景来说，我们的处理办法是:
# 在测试用例内写for循环去传参给具体的测试接口。
# 在有了parameters功能之后，我们只需要提供参数值，pytest帮我们完成for循环的动作。
# 这有个好处就是从读代码的人的角度来说，用例代码简单、清晰、明了。
@pytest.mark.parametrize(
    "test_input",
    ["a", "b", "c"]
)
def test_case_01(test_input):
    assert test_input in ("a", "b", "c")


# pytest在参数化方面，除了能传基础数据类型，也能传像字典这样的复合类型的值。
# 这个场景每次循环地传递一个字典给测试用例，测试用例内可以通过key的方式来读取到值。
@pytest.mark.parametrize(
    "test_input",
    [
        {"project_name": "pa01", "model_name": "po01"},
        {"project_name": "pa02", "model_name": "po02"},
        {"project_name": "pa03", "model_name": "po03"},
    ]
)
def test_case_02(test_input):
    assert test_input["project_name"] in ("pa01", "pa02", "pa03")


# 这个场景是两个参数和的多值场景。
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        ("2+4", 6),
        ("6*9", 54)
    ]
)
def test_case_03(test_input, expected):
    assert eval(test_input) == expected



