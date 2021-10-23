import random
from math import sqrt
from typing import List, Union

import timeit

def standard_deviation(inlist: List[Union[float, int]]) -> float:
    mean = (sum(inlist) / len(inlist))
    dividend = len(inlist) - 1
    deviation2 = sqrt(
        sum([(x - mean) ** 2 for x in inlist])
        / dividend
    )
    return round(deviation2, 3)
