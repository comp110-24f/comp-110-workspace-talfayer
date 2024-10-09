"""Summing the elements of a list using different loops"""

__author__ = "730646268"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        if len(vals) == 0:
            return 0.0
        else:
            sum += vals[index]
            index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for num in vals:
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for idx in range(0, (len(vals))):
        sum += vals[idx]
    return sum
