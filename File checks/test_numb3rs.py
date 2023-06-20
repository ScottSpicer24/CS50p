import numb3rs

def test_validate():
    assert numb3rs.validate('1.10.100.25.') == True
    assert numb3rs.validate('25.75.125.69.') == True
    assert numb3rs.validate('0.0.0.0.') == True
    assert numb3rs.validate('255.255.255.255.') == True
    assert numb3rs.validate('300.1.1.1.') == False
    assert numb3rs.validate('30.1.1.1') == False
    assert numb3rs.validate('1.1.1.') == False
    assert numb3rs.validate('f.t.x.c.') == False
    assert numb3rs.validate('bazs') == False