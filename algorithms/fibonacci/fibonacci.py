def fib(n: int) -> int:
    if n == 0:
        return 0
    y = 1
    z = 1
    x = 2
    for i in range(n - 2):
        y = x
        x = y + z
        z = y

    return z
