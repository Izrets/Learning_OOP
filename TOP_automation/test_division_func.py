from utils import division
import pytest

@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5), (20, 10, 2), (30, 3, 10),
                                                   (1, 0, ZeroDivisionError)])

# def test_division_good(a, b, expected_result):
#
#     assert division(a, b) == expected_result 

def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result

def test_zero_division(a, b, expected_result):
    assert division(a, b) == expected_result
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert division(1, 0)