def factorial_recursive(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("non-integer factorial")

    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("non-integer factorial")

    if n == 0:
        return 1
    if n == 1:
        return 1
    raise Exception("not yet implemented")
