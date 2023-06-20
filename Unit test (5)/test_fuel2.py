import fuel2

def test_convert():
    assert fuel2.convert('1/3') == 33
    assert fuel2.convert('1/100') == 1
    assert fuel2.convert('1/1') == 100

def test_gauge():
    assert fuel2.gauge('99') == 'F'
    assert fuel2.gauge('0') == "E"
    assert fuel2.gauge('50') == '50%'
    assert fuel2.gauge('33') == "33%"