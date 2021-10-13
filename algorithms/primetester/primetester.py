def primetester2(a: int) -> bool:
    if a <= 3:
        return a > 1
    if a % 2 == 0 or a % 3 == 0:
        return False
