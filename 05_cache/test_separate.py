

def test_case_04(request):
    assert request.config.cache.get("token", None) is not None
