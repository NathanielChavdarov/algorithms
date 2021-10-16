from typing import List, Union


def mean(inlist: List[Union[float, int]]) -> float:
    return sum(inlist) / len(inlist)
