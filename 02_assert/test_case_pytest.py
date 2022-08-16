




def test_case():
    assert 1 == 1
    assert "a" != "b"
    assert bool("a")
    assert not bool("")
    assert True is True
    assert True is not False
    assert None is None
    assert "a" is not None
    assert "a" in ("a", "b", "c")
    assert "a" not in ("b", "c", "d")
    assert isinstance("a", str)
    assert not isinstance(1, str)

    assert 1 > 0
    assert 1 >= 1
    assert 1 < 2
    assert 1 <= 1
