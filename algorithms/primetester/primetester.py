def primetester(input_num: int) -> bool:
    if input_num <= 3:
        return input_num > 1
    if input_num % 2 == 0 or input_num % 3 == 0:
        return False

    i = 5

    while i * i <= input_num:
        if input_num % i == 0 or input_num % (i + 2) == 0:
            return False
        i += 6
    return True
