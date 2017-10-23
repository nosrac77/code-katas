"""Functions that test the series_sum function."""


def test_one_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(1), "1.00")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(1) == '1.00'


def test_two_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(2), "1.25")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(2) == '1.25'


def test_three_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(3), "1.39")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(3) == '1.39'


def test_four_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(4), "1.49")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(4) == '1.49'


def test_five_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(5), "1.57")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(5) == '1.57'


def test_six_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(6), "1.63")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(6) == '1.63'


def test_seven_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(7), "1.68")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(7) == '1.68'


def test_eight_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(8), "1.73")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(8) == '1.73'


def test_nine_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(9), "1.77")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(9) == '1.77'


def test_ten_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(15), "1.94")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(15) == '1.94'


def test_eleven_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(39), "2.26")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(39) == '2.26'


def test_twelve_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(58), "2.40")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(58) == '2.40'


def test_thirteen_sum_series_code_wars():
    """Function that emulates test.assert_equals(series_sum(0), "0.00")
    from code wars."""
    from sum_terms import series_sum
    assert series_sum(0) == '0.00'


def test_fourteen_sum_series_code_wars():
    """Function that emulates random tests from code wars."""
    from sum_terms import series_sum
    from random import randint
    sol = lambda n: '0.00' if n == 0 else (lambda s: s[:-2]+"."+s[-2:])(str(int(round(sum([1.0/(1+i*3) for i in range(n)])*100))))
    for _ in range(40):
        n = randint(0, 100)
    assert series_sum(n) == sol(n)
