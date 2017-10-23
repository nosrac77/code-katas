"""Kata: Ones and Zeroes - Convert an array of binary numbers to an integer of that value.

#1 Best Practices Solution by andrewferk, hackstrider, datagram, and others.

def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)
"""


def binary_array_to_number(arr):
    return (int(''.join([str(n) for n in arr]), 2))
