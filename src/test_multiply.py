"""Functions that test the multiply function."""


def test_one_multiply_code_wars():
    """Function that emulates test.assert_equals(multiply(1,1)
    from code wars."""
    from multiply import multiply
    assert multiply(1, 1) == 1


def test_two_multiply_code_wars():
    """Function that emulates test.assert_equals(multiply(2,1)
    from code wars."""
    from multiply import multiply
    assert multiply(2, 1) == 2


def test_three_multiply_code_wars():
    """Function that emulates test.assert_equals(multiply(2,2)
    from code wars."""
    from multiply import multiply
    assert multiply(2, 2) == 4


def test_four_multiply_code_wars():
    """Function that emulates test.assert_equals(multiply(3,5)
    from code wars."""
    from multiply import multiply
    assert multiply(3, 5) == 15


# The tests below are mine.


def test_one_multiply_carson():
    """Function that checks return value of 25 when input is
    two fives."""
    from multiply import multiply
    assert multiply(5, 5) == 25


def test_two_multiply_carson():
    """Function that checks return value of 100 when input is
    two tens."""
    from multiply import multiply
    assert multiply(10, 10) == 100


def test_three_multiply_carson():
    """Function that checks return value of 10000 when input is
    one-hundred and one-hundred."""
    from multiply import multiply
    assert multiply(100, 100) == 10000


def test_four_multiply_carson():
    """Function that checks TypeError is raised when input is
    two strings."""
    from multiply import multiply
    try:
        assert multiply('string', 'string') == TypeError
    except TypeError:
        print('Cannot multiply string values.')
