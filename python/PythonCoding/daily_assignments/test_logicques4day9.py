import pytest

@pytest.mark.parametrize("num", [2,10,22])
def test_is_even(num):
    assert num % 2 == 0