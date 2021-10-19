import math

import pytest

from algorithms import factorial_iterative

def test_factorial_iterative_positive():
    answers = [
        (3, math.factorial(3)),
        (2, math.factorial(2)),
        (1, math.factorial(1)),
        (0, math.factorial(0)),
        (12, math.factorial(12)),
        (7.2, ValueError("non-integer factorial")),
    ]
    with pytest.raises(ValueError):
        for q, a in answers:
            assert factorial_iterative(q) == a

def test_factorial_iterative_negative():
    answers = [
        (-3, -6),
        (-2, 2),
        (-1, -1),
        (-12, 479001600),
        (-7.2, ValueError("non-integer factorial")),
    ]
    with pytest.raises(ValueError):
        for q, a in answers:
            assert factorial_iterative(q) == a
