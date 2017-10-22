"""Kata: Fibonacci's FizzBuzz - return a list of the fibonacci sequence with
the words 'Fizz', 'Buzz', and 'FizzBuzz' replacing certain integers.

#1 Best Practices Solution by damjan.

def fibs_fizz_buzz(n):
    a, b, out = 0, 1, []

    for i in range(n):
        s = "Fizz"*(b % 3 == 0) + "Buzz"*(b % 5 == 0)
        out.append(s if s else b)
        a, b = b, a+b

    return out
"""


def fibs_fizz_buzz(n):
    seq = [1, 1]
    x = 2
    if n == 1:
        return [1]
    while x <= n - 1:
        seq.append(seq[x - 1] + seq[x - 2])
        x += 1
    for idx, i in enumerate(seq):
        if i % 3 == 0 and i % 5 == 0:
            seq[idx] = 'FizzBuzz'
        elif i % 3 == 0:
            seq[idx] = 'Fizz'
        elif i % 5 == 0:
            seq[idx] = 'Buzz'
    return seq
