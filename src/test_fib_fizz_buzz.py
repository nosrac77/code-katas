"""Functions that test the likes function."""
import pytest


tests = [
    (2, [1, 1]),
    (5, [1, 1, 2, 'Fizz', 'Buzz']),
    (7, [1, 1, 2, 'Fizz', 'Buzz', 8, 13]),
    (10, [1, 1, 2, 'Fizz', 'Buzz', 8, 13, 'Fizz', 34, 'Buzz']),
    (15, [1, 1, 2, 'Fizz', 'Buzz', 8, 13, 'Fizz', 34, 'Buzz', 89, 'Fizz', 233, 377, 'Buzz']),
    (20, [1, 1, 2, "Fizz", "Buzz", 8, 13, "Fizz", 34, "Buzz", 89, "Fizz", 233, 377, "Buzz", "Fizz", 1597, 2584, 4181, "FizzBuzz"]),
    (1, [1]),
    (40, [1, 1, 2, "Fizz", "Buzz", 8, 13, "Fizz", 34, "Buzz", 89, "Fizz", 233, 377, "Buzz", "Fizz", 1597, 2584, 4181, "FizzBuzz", 10946, 17711, 28657, "Fizz", "Buzz", 121393, 196418, "Fizz", 514229, "Buzz", 1346269, "Fizz", 3524578, 5702887, "Buzz", "Fizz", 24157817, 39088169, 63245986, "FizzBuzz"]),
]


@pytest.mark.parametrize('n, result', tests)
def test_one_fib(n, result):
    """Function that emulates the 'Basic Tests' from code wars."""
    from fib_fizz_buzz import fibs_fizz_buzz
    assert fibs_fizz_buzz(n) == result


def test_two_fib():
    """Function that emulates the 'Random Tests' from code wars."""
    from fib_fizz_buzz import fibs_fizz_buzz
    from random import randint

    reference = lambda n: list(map(_fizz_buzz, _fib(n)))

    def _fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
            yield a

    def _fizz_buzz(n):
        if n % 15 == 0:
            return "FizzBuzz"
        if n % 5 == 0:
            return "Buzz"
        if n % 3 == 0:
            return "Fizz"
        return n

    for _ in range(100):
        test_case = randint(1, 1000)
        assert fibs_fizz_buzz(test_case) == reference(test_case)


def test_one_fib_carson():
    """Function that ensure input of string raises TypeError."""
    from fib_fizz_buzz import fibs_fizz_buzz
    try:
        assert fibs_fizz_buzz('string') == TypeError
    except TypeError:
        print('Cannot take string.')


def test_two_fib_carson():
    """Function that ensure input of float doesn't raise TypeError."""
    from fib_fizz_buzz import fibs_fizz_buzz
    assert fibs_fizz_buzz(1.0015) != TypeError


def test_three_fib_carson():
    """Function that ensure input of binary doesn't raise TypeError."""
    from fib_fizz_buzz import fibs_fizz_buzz
    assert fibs_fizz_buzz(0b1101) != TypeError


def test_four_fib_carson():
    """Function that ensure input of list raises TypeError."""
    from fib_fizz_buzz import fibs_fizz_buzz
    try:
        assert fibs_fizz_buzz([1]) == TypeError
    except TypeError:
        print('Cannot take list.')


def test_five_fib_carson():
    """Function that ensure input of tuple doesn't raise TypeError."""
    from fib_fizz_buzz import fibs_fizz_buzz
    assert fibs_fizz_buzz((3)) != TypeError
