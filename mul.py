# mulPeasant multiplies two integers using Peasant multiplication
# https://en.wikipedia.org/wiki/Multiplication_algorithm#Binary_or_Peasant_multiplication
def mulPeasant(a: int, b: int) -> int:
    result: int = 0

    while a > 0:
        if a % 2 == 1:
            result += b
        a >>= 1
        b <<= 1

    return result
