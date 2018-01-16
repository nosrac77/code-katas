"""Functions that test the disemvowel function."""


def test_one_disemvowel_code_wars():
    """This function emulates basic tests from code wars."""
    from disemvowel_trolls import disemvowel
    tests = [("This website is for losers LOL!", "Ths wbst s fr lsrs LL!"),
             ("No offense but,\nYour writing is among the worst I've everread",
             "N ffns bt,\nYr wrtng s mng th wrst 'v vrrd"),
             ("What are you, a communist?", "Wht r y,  cmmnst?")]

    for case in tests:
        assert disemvowel(case[0]) == case[1]


def test_one_disemvowel_carson():
    """Function that checks returned string has all vowels removed."""
    from disemvowel_trolls import disemvowel
    assert disemvowel('Successiuoaeeeouiiiea') == 'Sccss'


def test_two_disemvowel_carson():
    """Function that checks returned string is empty."""
    from disemvowel_trolls import disemvowel
    assert disemvowel('oeeoeeoeaaaaiiiiiii') == ''


def test_three_disemvowel_carson():
    """Function that ensures input of binary raises TypeError."""
    from disemvowel_trolls import disemvowel
    try:
        assert disemvowel(0b1101) == TypeError
    except TypeError:
        print('Cannot take binary numbers!')


def test_four_disemvowel_carson():
    """Function that ensures input of list still removes vowels."""
    from disemvowel_trolls import disemvowel
    assert disemvowel(['eeeeeeeeeeee']) == 'eeeeeeeeeeee'
