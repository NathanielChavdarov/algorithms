def factorial_iterative(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("non-integer factorial")

    if n == 0:
        return 1
    if n == 1:
        return 1

    if n > 0:
        factorial_split = [x for x in range(n, 1, -1)]
    elif n < 0:
        factorial_split = [x for x in range(n, 0, +1)]

    sum_factorial = 1

    for val in range(len(factorial_split)):
        sum_factorial = sum_factorial * factorial_split[val]

    return sum_factorial
