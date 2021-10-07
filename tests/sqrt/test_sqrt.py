import pytest

from algorithms import sqrt


def test_sqrt():
    answers = [
        (4, 2),
        (16, 4),
        (6.25, 2.5),
    ]
    for q, a in answers:
        assert sqrt(q, 55) == a


def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-4, 55)
