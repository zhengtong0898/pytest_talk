

token = '7e6a9597831c4dffb4ce9c6404816069'


def test_case_01(request):
    request.config.cache.set("token", token)                        # 创建缓存
    assert request.config.cache.get("token", None) == token         # 读取缓存


def test_case_02(request):
    assert request.config.cache.get("token", None) == token         # 读取缓存, 期望与token一致
    request.config.cache.set("token", None)                         # 重置缓存


def test_case_03(request):
    assert request.config.cache.get("token", None) is None          # 读取缓存, 期望是空
    request.config.cache.set("token", token)                        # 再次把缓存写回去
    assert request.config.cache.get("token", None) == token
