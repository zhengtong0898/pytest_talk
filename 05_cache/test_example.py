import uuid


token = uuid.uuid4().hex


def test_case_01(request):
    request.config.cache.set("token", token)                        # 创建缓存
    assert request.config.cache.get("token", None) == token         # 读取缓存


def test_case_02(request):
    assert request.config.cache.get("token", None) == token         # 读取缓存, 期望与token一致
    request.config.cache.set("token", None)                         # 重置缓存


def test_case_03(request):
    assert request.config.cache.get("token", None) is None          # 读取缓存, 期望是空
