import os

from algorithms import primetester


def test_primetester():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "primes.txt")) as fhandle:
        line = fhandle.readline()
    primes = [int(x) for x in line.split(",")]
    for number in range(primes[-1] + 2):
        got = primetester(number)
        expected = number in primes
        assert (
            got == expected
        ), f"number={number}, got={got}, expected={expected}"
