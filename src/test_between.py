"""Functions that test the between function"""


def test_one_between_code_wars():
    """Function that emulates test.expect(between(1,4)) from code wars"""
    from between import between
    assert between(1, 4) == [1, 2, 3, 4]


def test_two_between_code_wars():
    """Function that emulates test.expect(between(5,500)) from code wars"""
    from between import between
    assert between(5, 500) == [x for x in range(5, 500 + 1)]


def test_three_between_code_wars():
    """Function that emulates test.expect(between(-10,10)) from code wars"""
    from between import between
    assert between(-10, 10) == [x for x in range(-10, 10 + 1)]


def test_four_between_code_wars():
    """Function that emulates test.expect(between(-2,2)) from code wars"""
    from between import between
    assert between(-2, 2) == [x for x in range(-2, 2 + 1)]


# Tests below are mine.


def test_one_between_carson():
    """Function that tests if between function can take binary values."""
    from between import between
    assert between(0b1, 0b1100) == [x for x in range(1, 12 + 1)]


def test_two_between_carson():
    """Function that tests if between function raises TypeError when
    given float values."""
    from between import between
    try:
        assert between(1.4, 9.9) == [x for x in range(1, 10 + 1)]
    except TypeError:
        print('Cannot take float values.')


def test_three_between_carson():
    """Function that tests if between function raises TypeError when
    given string values."""
    from between import between
    try:
        assert between('hello', 'world') == TypeError
    except TypeError:
        print('Cannot take string values.')


def test_four_between_carson():
    """Function that tests if between function raises TypeError when
    given list values."""
    from between import between
    try:
        assert between([1, 3, 5], [3, 6, 9]) == TypeError
    except TypeError:
        print('Cannot take list values.')
