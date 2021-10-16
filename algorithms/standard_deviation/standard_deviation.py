from typing import List, Union
from math import sqrt


def standard_deviation(inlist: List[Union[float, int]]) -> float:
    deviation2 = sqrt(
        sum([(x - sum(inlist) / len(inlist)) ** 2 for x in inlist])
        / (len(inlist) - 1)
    )
    return round(deviation2, 3)
