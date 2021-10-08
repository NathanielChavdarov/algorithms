from algorithms import fib

answers = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (20, 6765),
    (30, 832040),
]


def test_fibonacci():
    # The slow function
    for i, fib_i in answers:
        assert fib(i) == fib_i
