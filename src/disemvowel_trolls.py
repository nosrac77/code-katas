"""Kata: Disemvowel Trolls - return a string with the values of the given
string removed.

#1 Best Practices Solution by cvk77, zyrolasting, sneakybueno.

def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
"""


def disemvowel(string):
    return ''.join([x for x in string if x != 'O' and x != 'o' and x != 'a' and x != 'A' and x != 'i' and x != 'I' and x != 'e' and x != 'E' and x != 'u' and x != 'U'])
