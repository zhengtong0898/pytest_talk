

def test_case_01(request):
    assert request.config.inicfg["ssh_username"] == "root"
