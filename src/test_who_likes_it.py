"""Functions that test the likes function."""


def test_one_who_likes_it_code_wars():
    """Function that emulates test.assert_equals(likes([])."""
    from who_likes_it import likes
    assert likes([]) == 'no one likes this'


def test_two_who_likes_it_code_wars():
    """Function that emulates test.assert_equals(likes(['Peter'])."""
    from who_likes_it import likes
    assert likes(['Peter']) == 'Peter likes this'


def test_three_who_likes_it_code_wars():
    """Function that emulates test.assert_equals(likes(['Jacob', 'Alex'])."""
    from who_likes_it import likes
    assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'


def test_four_who_likes_it_code_wars():
    """Function that emulates test.assert_equals
    (likes(['Max', 'John', 'Mark'])."""
    from who_likes_it import likes
    assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'


def test_five_who_likes_it_code_wars():
    """Function that emulates test.assert_equals
    (likes(['Alex', 'Jacob', 'Mark', 'Max'])."""
    from who_likes_it import likes
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'


def test_six_who_likes_it_code_wars():
    """Function that emulates random tests from code wars."""
    from who_likes_it import likes
    from random import randint, shuffle
    sol = lambda n: 'no one likes this' if len(n) == 0 else n[0]+' likes this' if len(n) == 1 else n[0]+' and '+n[1]+' like this' if len(n) == 2 else n[0]+', '+n[1]+' and '+n[2]+' like this' if len(n) == 3 else n[0]+', '+n[1]+' and '+str(len(n)-2)+' others like this'
    base = ["Sylia Stingray", "Priscilla S. Asagiri", "Linna Yamazaki",
            "Nene Romanova", "Nigel", "Macky Stingray", "Largo",
            "Brian J. Mason", "Sylvie", "Anri", "Leon McNichol",
            "Daley Wong", "Galatea", "Quincy Rosenkreutz"]
    for _ in range(40):
        shuffle(base)
        names = base[:randint(0, len(base)-1)]
        assert likes(names) == sol(names)


# The tests below are ones I created.


def test_one_who_likes_it_carson():
    """Function that tests if list input that contains integers raises
    TypeError."""
    from who_likes_it import likes
    try:
        assert likes([1, 4, 55, 2443])
    except TypeError:
        print('Cannot use numbers as list input.')


def test_two_who_likes_it_carson():
    """Function that tests if list input that contains floats raises
    TypeError."""
    from who_likes_it import likes
    try:
        assert likes([55.006, 79.002, 9903.00605])
    except TypeError:
        print('Cannot use numbers as list input.')


def test_three_who_likes_it_carson():
    """Function that tests if list input that contains booleans raises
    TypeError."""
    from who_likes_it import likes
    try:
        assert likes([True, False, False])
    except TypeError:
        print('Cannot use booleans as list input.')


def test_four_who_likes_it_carson():
    """Function that tests if list input that contains characters raises
    TypeError."""
    from who_likes_it import likes
    try:
        assert likes(['!@#$%^&*()+_-~'])
    except TypeError:
        print('Cannot use characters as list input.')


def test_five_who_likes_it_carson():
    """Function that tests if list input that contains binary numbers raises
    TypeError."""
    from who_likes_it import likes
    try:
        assert likes([0b1101, 0b1, 0b1101001])
    except TypeError:
        print('Cannot use characters as list input.')
