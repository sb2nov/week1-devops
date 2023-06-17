from calculator import add,mul,sub,div

def test_add():
    assert add(1,1) ==0

def test_mul():
    assert mul(2,3) ==6

def test_sub():
    assert sub(4,2) ==2

def test_div():
    assert div(6,3) ==2