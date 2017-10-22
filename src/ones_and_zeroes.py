"""Kata: Fibonacci's FizzBuzz - return a list of the fibonacci sequence with
the words 'Fizz', 'Buzz', and 'FizzBuzz' replacing certain integers.

#1 Best Practices Solution by andrewferk, hackstrider, datagram, and others.

def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)
"""


def binary_array_to_number(arr):
    return (int(''.join([str(n) for n in arr]), 2))
