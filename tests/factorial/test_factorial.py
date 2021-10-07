import factorial as f
import math
import pytest

answers = [
	(0, 1),
	(1, 1),
	(4, math.factorial(4)),
	(164, math.factorial(164)),
	(7.2, ValueError("Factorial only supports integers!")),
]


def test_factorial():
	with pytest.raises(ValueError):
		"Factorial only supports integers!"
		for q, a in answers:
			assert f.factorial(q) == a
