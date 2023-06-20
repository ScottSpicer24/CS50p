import response

def test_valid():
    assert response.valid("scott@gmail.com") == "Valid"
    assert response.valid("scott@gmail.edu") == "Valid"
    assert response.valid("scott@@@gmail.com") == "Invalid"
    assert response.valid("scott@gmail..com") == "Invalid"
    assert response.valid("scott@gmail.con") == "Invalid"