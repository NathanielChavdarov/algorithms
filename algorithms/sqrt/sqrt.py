def sqrt(n: float, precision: int) -> float:
    if n < 0:
        raise ValueError("Cannot find square root of a negative number!")
    if n in (0, 1):
        return n  # Sqrt of 0 = 0 and sqrt of 1 = 1 so we return the number

    if int(n) == n:  # Checks if the input number is an integer
        for i in range(1, int(n)):
            if i * i == n:
                # print(f"The number {n} is a square number")
                return i  # Return the square root of the number
            if i * i > n:
                break
    if n < 1:
        lbound = n
        ubound = 1.0
    else:
        lbound = 1.0
        ubound = n
    count = 0
    while True:
        count += 1
        mpoint = (ubound + lbound) / 2  # Finds the half-way point
        # print(f"lbound = {lbound}, ubound = {ubound}, mpoint = {mpoint}")
        if mpoint * mpoint > n:
            ubound = mpoint
        elif mpoint * mpoint == n:
            return mpoint
        else:
            lbound = mpoint
        if count > precision:  # Stops the algorithm once precision is reached
            return mpoint
