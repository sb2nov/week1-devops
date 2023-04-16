# Demo Calculator App For Week 1 Project
# Addition Method
def add(a, b):
    return (a + b)

# Subtract Method
def sub(a, b):
    return (a - b)

# Multiplication
def mul(a, b):
    return (a * b)

# Division
def div(a,b):
    return (a/b)

def test_add():
    assert add(1,1) == 2

def test_sub():
    assert sub(1,1) == 0

def test_mul():
    assert mul(1,1) == 1

def test_div():
    assert div(2,1) == 2

if __name__ == "__main__":
    # Declare variable and set default values
    a = 4
    b = 2
    print('Sum of ' + str(a) + ' and ' + str(b) + ' is ', add(a, b))
    print('Difference of ' + str(a) + ' and ' + str(b) + ' is ', sub(a, b))
    print('Product of ' + str(a) + ' and ' + str(b) + ' is ', mul(a, b))
    print('Division of ' + str(a) + ' and ' + str(b) + ' is ', div(a, b))