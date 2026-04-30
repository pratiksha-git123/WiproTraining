import pytest

def test_sum():
    assert 3 + 5 == 8

def test_upper_fail():
    assert "hello".upper() == "hello"

@pytest.fixture
def sample_list():
    return[1, 2, 3]

def test_list_length(sample_list):
    assert len(sample_list) == 3

def square(x):
    return x * x

@pytest.mark.parametrize("input, expected",
                         [(2, 4),(3, 9),(4, 16)])
def test_square(input, expected):
    assert square(input) == expected

def divide(a, b):
    return a / b
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
