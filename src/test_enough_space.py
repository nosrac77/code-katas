"""Functions that test the enough function."""


def test_one_enough_code_wars():
    """Function that emulates test.assert_equals(enough(10, 5, 5))
    from code wars."""
    from enough_space import enough
    assert enough(10, 5, 5) == 0


def test_two_enough_code_wars():
    """Function that emulates test.assert_equals(enough(100, 60, 50))
    from code wars."""
    from enough_space import enough
    assert enough(100, 60, 50) == 10


# Tests below are mine.


def test_one_enough_carson():
    """Function that checks return value of 1."""
    from enough_space import enough
    assert enough(10, 9, 2) == 1


def test_two_enough_carson():
    """Function that checks return value of 100 when input is
    two tens."""
    from enough_space import enough
    assert enough(10, 9, 2) == 1


def test_three_enough_carson():
    """Function that checks return value of 0."""
    from enough_space import enough
    assert enough(100, 60, 0) == 0


def test_four_enough_carson():
    """Function that checks return value is not -10."""
    from enough_space import enough
    assert enough(1000, 50, 50) != -10
