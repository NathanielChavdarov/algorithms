from typing import Any, List


def bubble_sort(alist: List[Any]) -> List[Any]:
    if alist is None:
        return alist
    a = len(alist)
    if a <= 1:
        return alist

    for j in range(a - 1, 1, -1):
        for i in range(0, j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

    return alist
