def picalc(p: int) -> float:
    counter = 0
    x = 0
    pp = p*p
    while x <= p: #
        y = 0
        xx = x*x
        while y <= p:
            yy = y*y
            d = xx + yy
            if d <= pp:
                counter += 1
            y += 1
        x += 1
    pi = counter * 4 / pp
    return pi
