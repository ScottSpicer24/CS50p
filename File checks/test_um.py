import um

def test_count():
    assert um.count("um") == 1
    assert um.count("um, yes") == 1
    assert um.count("um... no") == 1
    assert um.count("I um guess") == 1
    assert um.count("um if you um say so") == 2
    assert um.count("yummy") == 0
    assert um.count("yum") == 0