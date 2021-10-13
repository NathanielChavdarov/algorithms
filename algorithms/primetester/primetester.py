def primetester2(a: int) -> bool:
    if a <= 3:
        return a > 1
    if a % 2 == 0 or a % 3 == 0:
        return False

    i = 5

    while i * i <= a:
        if a % i == 0 or a % (i + 2) == 0:
            return False
        i += 6
    return Truyepe
