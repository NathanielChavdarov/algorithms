def fib(fib_number: int) -> int:
    if fib_number == 0:
        return 0
    num_1 = 1
    num_2 = 1
    num_3 = 2
    for _ in range(fib_number - 2):
        num_1 = num_3
        num_3 = num_1 + num_2
        num_2 = num_1

    return num_2
