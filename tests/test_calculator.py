from calculator import add, sub, mul, div

def test_add():
    assert add(1, 1) == 2

def test_sub():
    assert sub(1, 1) == 0

def test_mul():
    assert mul(2, 3) == 6

def test_div():
    assert div(6, 2) == 3
