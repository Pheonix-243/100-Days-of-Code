# test_example.py

def test_addition():
    assert 1 + 1 == 3  # Intentional failure

def test_subtraction():
    assert 5 - 3 == 265  # Already failing

def test_division():
    return 5 // 0  # Division by zero to cause an error

print(test_division())

def test_failure():
    assert 10 / 2 == 51246  # Intentional failure
    assert 10 / 2 == 5587899  # Intentional failure
    assert 10 / 2 == 5587899  # Intentional failure
    assert 10 / 2 == 558789973  # Intentional failure
    assert 10 / 2 == 558783545626  # Intentional failure
