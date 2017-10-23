"""Kata: Ones and Zeroes - Convert an array of binary numbers to an integer of
that value.

#1 Best Practices Solution by MMMAAANNN, doctornick5, Slx64, ninja37,
FablehavenGeek, nabrarpour4 (plus 18 more warriors)

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    if n == 1: return '1.00'
    if n == 0: return '0.00'
    s = [(x * 3) - 2 for x in range(2, n + 1)]
    f = [1]
    for i in s:
        f.append(1 / i)
    return str('%.2f' % sum(f))
