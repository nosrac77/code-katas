"""Functions that test array_diff function."""
import pytest


def test_one_array_diff_code_wars():
    """Test function that emulates test.assert_equals(array_diff([1,2], [1])."""
    from array_diff import array_diff
    assert array_diff([1, 2], [1]) == [2]


def test_two_array_diff_code_wars():
    """Test function that emulates test.assert_equals(array_diff([1,2], [1])."""
    from array_diff import array_diff
    assert array_diff([1, 2], [1]) == [2]


def test_three_array_diff_code_wars():
    """Test function that emulates test.assert_equals(array_diff([1,2,2], [1])."""
    from array_diff import array_diff
    assert array_diff([1, 2, 2], [1]) == [2, 2]


def test_four_array_diff_code_wars():
    """Test function that emulates test.assert_equals(array_diff([1,2,2], [2])."""
    from array_diff import array_diff
    assert array_diff([1, 2, 2], [2]) == [1]


def test_five_array_diff_code_wars():
    """Test function that emulates test.assert_equals(array_diff([1,2,2], [])."""
    from array_diff import array_diff
    assert array_diff([1, 2, 2], []) == [1, 2, 2]


def test_six_array_diff_code_wars():
    """Test function that emulates test.assert_equals(array_diff([], [1,2])."""
    from array_diff import array_diff
    assert array_diff([], [1, 2]) == []


def test_seventh_array_diff_code_wars():
    """Test function that emulates randint tests."""
    from array_diff import array_diff
    from random import randint

    def array_sol(a, b): return [item for item in a if item not in b]
    for _ in range(40):
        alen, blen = randint(0, 20), randint(0, 20)
        a = [randint(0, 40)-20 for i in range(alen)]
        b = [randint(0, 40)-20 for i in range(blen)]
    assert array_diff(a, b) == array_sol(a, b)


# The tests below are ones I created.


def test_one_array_diff_carson():
    """Test function that checks if array_diff returns [-1]."""
    from array_diff import array_diff
    assert array_diff([1, -1], [1]) == [-1]


def test_two_array_diff_carson():
    """Test function that checks if array_diff returns ['a']."""
    from array_diff import array_diff
    assert array_diff(['a', 'b'], ['b']) == ['a']


def test_three_array_diff_carson():
    """Test function that checks if array_diff returns []."""
    from array_diff import array_diff
    assert array_diff(['a', 1], [1, 'a']) == []


def test_four_array_diff_carson():
    """Test function that ensures input of boolean values
    raises AssertionError."""
    from array_diff import array_diff
    try:
        assert array_diff(['a', 1, 'b', True], ['b', 1, 'a']) == AssertionError
    except AssertionError:
        print('Cannot use boolean values.')
