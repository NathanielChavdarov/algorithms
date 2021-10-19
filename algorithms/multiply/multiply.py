def mul_peasant(first_value: int, second_value: int) -> int:
    """
    Multiply two integers using Peasant multiplication
    https://en.wikipedia.org/wiki/Multiplication_algorithm
    """
    result: int = 0

    while first_value > 0:
        if first_value % 2 == 1:
            result += second_value
        first_value >>= 1
        second_value <<= 1

    return result
