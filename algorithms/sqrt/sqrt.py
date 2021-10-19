def sqrt(input_num: float, precision: int) -> float:
    if input_num < 0:
        raise ValueError("Cannot find square root of a negative number!")
    if input_num in (0, 1):
        return input_num

    if int(input_num) == input_num:  # Checks if the input number is an integer
        for i in range(1, int(input_num)):
            if i * i == input_num:
                # print(f"The number {input_num} is a square number")
                return i  # Return the square root of the number
            if i * i > input_num:
                break
    if input_num < 1:
        lbound = input_num
        ubound = 1.0
    else:
        lbound = 1.0
        ubound = input_num
    count = 0
    while True:
        count += 1
        mpoint = (ubound + lbound) / 2  # Finds the half-way point
        # print(f"lbound = {lbound}, ubound = {ubound}, mpoint = {mpoint}")
        if mpoint * mpoint > input_num:
            ubound = mpoint
        elif mpoint * mpoint == input_num:
            return mpoint
        else:
            lbound = mpoint
        if count > precision:  # Stops the algorithm once precision is reached
            return mpoint
