"""Kata: Sort a Deck of Cards - my task was the sort a given list of unicode
characters based upon their card value. After seeing the solution, I'm not
proud of my answer.

#1 Best Practices Solution by zebulan, Unnamed, acaccia, j_codez, Mr.Child,
iamchingel (plus 7 more warriors)

def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)
"""


def sort_cards(cards):
    return [x for x in cards if x == 'A'] + sorted([x for x in cards if x not in 'ATJKQ']) + sorted([x for x in cards if x in 'TJ'], reverse=True) + sorted([x for x in cards if x in 'QK'], reverse=True)
