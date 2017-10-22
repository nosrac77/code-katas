"""Kata: Will there be enough space - return integer given set of three
integers.

#1 Best Practices Solution by vaskinyy, AlexBaier, DCoulter

def enough(cap, on, wait):
    return max(0, wait - (cap - on))
"""


def enough(cap, on, wait):
    if on + wait == cap: return 0
    if (cap - on) > wait: return 0
    return wait - (cap - on)
