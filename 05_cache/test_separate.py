

token = '7e6a9597831c4dffb4ce9c6404816069'


def test_case_04(request):
    assert request.config.cache.get("token", None) == token
