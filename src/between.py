"""Kata: Test between - return array of integers between a and b.

#1 Best Practices Solution by zebulan, lancelote, Paulchenkiller,
antoine.leclercq, VadimPopov, Jonathan.Chan (plus 93 more warriors)

def between(a,b):
    return range(a,b+1)
"""


def between(a, b):
    return ([x for x in range(a, b+1)])
