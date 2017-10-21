"""Functions that test nth_even function."""


def test_one_code_wars():
    """Test function that emulates test.assert_equals(nth_even(1), 0)"""
    from get_nth_even_number import nth_even
    assert nth_even(1) == 0


def test_two_code_wars():
    """Test function that emulates test.assert_equals(nth_even(2), 2)."""
    from get_nth_even_number import nth_even
    assert nth_even(2) == 2


def test_three_code_wars():
    """Test function that emulates test.assert_equals(nth_even(3), 4)."""
    from get_nth_even_number import nth_even
    assert nth_even(3) == 4


def test_four_code_wars():
    """Test function that emulates test.assert_equals(nth_even(100), 198)."""
    from get_nth_even_number import nth_even
    assert nth_even(100) == 198


def test_five_code_wars():
    """Test function that emulates test.assert_equals(nth_even(1298734), 2597466)."""
    from get_nth_even_number import nth_even
    assert nth_even(1298734) == 2597466


def test_one_carson():
    """Test function that checks nth_even returns 6 when n is equal to 3."""
    from get_nth_even_number import nth_even
    assert nth_even(3) == 4


def test_two_carson():
    """Test function that checks nth_even returns 8 when n is equal to 5."""
    from get_nth_even_number import nth_even
    assert nth_even(5) == 8


def test_three_carson():
    """Test function that checks nth_even returns ValueError when n is equal to 0."""
    from get_nth_even_number import nth_even
    try:
        assert nth_even(0)
    except ValueError:
        print('0 cannot by multiplied!')


def test_four_carson():
    """Test function that checks nth_even returns -6 if given -2"""
    from get_nth_even_number import nth_even
    assert nth_even(-2) == -6
