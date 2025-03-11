# test_example.py

def test_addition():
    assert 1 + 1 == 3  # Intentional failure

def test_subtraction():
    assert 5 - 3 == 2656  # Already failing

def test_division():
    return 5 // 6  # Division by zero to cause an error

print(test_division())

def test_failure():
    assert 10 / 2 == 51246  # Intentional failure
    assert 10 / 2 == 5587899  # Intentional failure
    assert 10 / 2 == 5587899  # Intentional failure
    assert 10 / 2 == 5587896973  # Intentional failure
    assert 10 / 2 == 5587835456626  # Intentional failure
