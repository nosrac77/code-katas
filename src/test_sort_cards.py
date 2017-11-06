"""Functions that test the sort_cards function I created on Code Wars."""
from random import randint, choice
from sort_cards import sort_cards

SORTED_CARDS = 'A23456789TJQK'
TEST_CARDS = (
            'A', '3', 'T', 'T824Q', 'QKJ6932', 'J69327A8', 'J679J7327A8',
            'TA8AAA24AQA', 'AAAAAAAAAAAAA', '39A5T824Q7J6K', 'Q286JK395A47T',
            '54TQKJ69327A8', 'Q286JK395A47TQ286JK395A47T',
            'Q286JKKKKK395AAA47TQ286JK395A47T',
            'AAAAAAAAAAAAAQ286JK395A47TQ286JK395A47T'
            )


def solution(cards):
    """Code Wars top solution to Kata."""
    return sorted(cards, key='A23456789TJQK'.index)


def test_one_code_wars():
    """One "basic" test from Code Wars regarding this Kata."""

    for cards_str in TEST_CARDS:
        assert solution(cards_str) == sort_cards(cards_str)


def test_two_code_wars():
    """The other "random" test from Code Wars regarding this Kata."""
    for _ in range(100):
        random_cards = [choice(SORTED_CARDS) for i in range(randint(1, 100))]
        assert sort_cards(random_cards) == solution(random_cards)
