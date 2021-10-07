import picalc as p

answers = [
	(10, 3, 4),
	(100, 3.1, 3.2),
	(1000, 3.14, 3.15),
	(5000, 3.142, 3.143),
]

def test_picalc():
	for i, l, u in answers:
		assert p.picalc(i) > l and p.picalc(i) < u
