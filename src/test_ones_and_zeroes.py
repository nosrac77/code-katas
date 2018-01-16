"""Functions that test the disemvowel function."""


def test_one_ones_and_zeroes_code_wars():
    """Function that emulates test.assert_equals
    (binary_array_to_number([0,0,0,1]))"""
    from ones_and_zeroes import binary_array_to_number
    assert binary_array_to_number([0, 0, 0, 1]) == 1


def test_two_ones_and_zeroes_code_wars():
    """Function that emulates test.assert_equals
    (binary_array_to_number([0,0,1,0]))"""
    from ones_and_zeroes import binary_array_to_number
    assert binary_array_to_number([0, 0, 1, 0]) == 2


def test_three_ones_and_zeroes_code_wars():
    """Function that emulates test.assert_equals
    (binary_array_to_number([1,1,1,1]))"""
    from ones_and_zeroes import binary_array_to_number
    assert binary_array_to_number([1, 1, 1, 1]) == 15


def test_four_ones_and_zeroes_code_wars():
    """Function that emulates test.assert_equals
    (binary_array_to_number([0,1,1,0]))"""
    from ones_and_zeroes import binary_array_to_number
    assert binary_array_to_number([0, 1, 1, 0]) == 6


def test_five_ones_and_zeroes_code_wars():
    """Function that emulates test.assert_equals
    (binary_array_to_number([0,1,1,0]))"""
    from ones_and_zeroes import binary_array_to_number
    import random
    for _ in range(50):
        n = random.randint(0, 1000)
        array = [int(x) for x in bin(n)[2:]]
        assert binary_array_to_number(array) == n


# The tests below are mine.


def test_one_ones_and_zeroes_carson():
    """Function that tests ones_and_zeroes for binary values."""
    from ones_and_zeroes import binary_array_to_number
    assert binary_array_to_number([0b1, 0b1]) == 3


def test_two_ones_and_zeroes_carson():
    """Function that tests ones_and_zeroes for ValueError when
    tuple within list input."""
    from ones_and_zeroes import binary_array_to_number
    try:
        assert binary_array_to_number([(1, 1, 0, 1)]) == 11
    except ValueError:
        print('Tuples not allowed.')


def test_three_ones_and_zeroes_carson():
    """Function that tests ones_and_zeroes for ValueError when
    float values within list input."""
    from ones_and_zeroes import binary_array_to_number
    try:
        assert binary_array_to_number([1.2, 1, 1.2, 1.0]) == ValueError
    except ValueError:
        print('Floats not allowed.')


def test_four_ones_and_zeroes_carson():
    """Function that tests ones_and_zeroes for ValueError when
    multiple lists within list input."""
    from ones_and_zeroes import binary_array_to_number
    try:
        assert binary_array_to_number([[1], [0], [1]]) == ValueError
    except ValueError:
        print('Multiple lists not allowed.')
