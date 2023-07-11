from True2chisla import Dvachisla
import pytest

@pytest.mark.parametrize("a, b, expected_result", [([1, 2, 3, 4, 5], [1, 2, 9, 7], True)])

def test_true2ch_pytest_good(a, b, expected_result):
        action = Dvachisla()
        actiontoassert = action.inputOfTwo(a, b)
        assert actiontoassert == expected_result

