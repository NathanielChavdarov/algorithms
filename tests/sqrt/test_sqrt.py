import sqrt as s
import pytest

answers = [
	(4, 2),
	(16, 4),
	(6.25, 2.5),
	(-4, ValueError("Cannot find square root of a negative number!")),
]


def test_sqrt():
	with pytest.raises(ValueError):
		"Cannot find square root of a negative number!"
		for q, a in answers:
			assert s.sqrt(q, 55) == a
