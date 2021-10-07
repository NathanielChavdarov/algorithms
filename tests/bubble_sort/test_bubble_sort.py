import bubble_sort as bs
import pytest

answers = [
	([], []),
	([1], [1]),
	([1, 9, 2, 8, 3, 7, 4, 6, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
	(['abc', 'cba', 'aaa', 'ccc', 'bbb'], ['aaa', 'abc', 'bbb', 'cba', 'ccc']),
	([6.42, 7.1, 1.4, 9.26, 6.4], [1.4, 6.4, 6.42, 7.1, 9.26]),
]


def test_bubble_sort():
		for q, a in answers:
			assert bs.sort(q) == a
