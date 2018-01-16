"""Kata: Array diff - Subtract one list from another.

#1 Best Practices Solution by jmc04, JS01, javafreak, and others.

def array_diff(a, b):
    return [x for x in a if x not in b]
"""


def array_diff(a, b):
    return [item for item in a if item not in b]
