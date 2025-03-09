# test_example.py

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

# def test_failure():
#     assert 10 / 2 == 4  # This test will fail


def test_failure():
    assert 10 / 2 == 5  # This test will now pass