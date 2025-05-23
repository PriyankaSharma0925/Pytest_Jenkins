import pytest


def add(a, b):
    return a + b


def add_three_number(a, b, c):
    return a + b + c


def addition(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def pow(a, b):
    return a**b


### Parameterize fixture ###





##############################################################################


@pytest.mark.parametrize("base,expected", [(3, 9), (4, 16)])
def test_power(base, expected):
    assert base**2 == expected


def test_add_parameters(add_parameters):
    a, b, expected = add_parameters
    assert add(a, b) == expected, "This is correct"




def test_add():

    assert add(2, 5) == 7, "This is correct" "This is False"


@pytest.mark.skip
def test_add_three_number():
    assert add_three_number(2, 5, 3) == 10, "This is correct" "This is False"


@pytest.mark.skip
def test_addition():
    assert add_three_number(2, 5, 3) == 10, "This is correct" "This is False"


def test_substract():
    assert sub(9, 5) == 4, "Correct, 9 - 5 is 4" "False 9-5 is not 5"



def test_division():
    assert div(10, 2) == 5, "Correct, 10 / 2 is 5" "False 10 / 2 is not 5"


def test_pow():

    assert pow(10, 2) == 100, "Correct, 10 % 2 is 100" "False 10 % 2 is not 100"
