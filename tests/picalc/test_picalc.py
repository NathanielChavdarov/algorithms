from algorithms import picalc


def test_picalc():
    answers = [
        (10, 3, 4),
        (100, 3.1, 3.2),
        (1000, 3.14, 3.15),
        (5000, 3.142, 3.143),
    ]
    for i, l, u in answers:
        assert picalc(i) > l and picalc(i) < u
