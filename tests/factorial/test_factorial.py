import math

import pytest

from algorithms import factorial_iterative, factorial_recursive


@pytest.mark.skip("not yet implemented")
def test_factorial_iterative():
    answers = [
        (0, 1),
        (1, 1),
        # TODO ...
    ]
    for q, a in answers:
        assert factorial_iterative(q) == a


@pytest.mark.skip("not yet implemented")
def test_factorial_iterative_negative():
    pass
    # TODO ...
    # with pytest.raises(ValueError):
    #     factorial_iterative(7.2)


def test_factorial_recursive():
    answers = [
        (0, 1),
        (1, 1),
        (4, math.factorial(4)),
        (64, math.factorial(64)),
    ]
    for q, a in answers:
        assert factorial_recursive(q) == a


def test_factorial_recursive_negative():
    # Factorial only supports integers!
    with pytest.raises(ValueError):
        factorial_recursive(7.2)
