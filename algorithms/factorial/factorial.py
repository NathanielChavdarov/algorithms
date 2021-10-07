def factorial_recursive(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("non-integer factorial")

    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("non-integer factorial")

    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        raise Exception("not yet implemented")
