import working

def test_working():
    assert working.convert("5:30 AM to 2:45 AM") == "5:30 to 2:45"
    assert working.convert("8:34 AM to 1:23 PM") == "8:34 to 13:23"
    assert working.convert("12:36 PM to 1:56 AM") == "12:36 to 1:56"
    assert working.convert("8:30 PM to 10:45 PM") == "20:30 to 22:45"
    assert working.convert("8 AM to 10 PM") == "8 to 22"
    assert working.convert("1 AM to 13 PM") == ValueError