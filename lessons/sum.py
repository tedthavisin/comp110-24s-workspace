"""Summing the elements of a list using different loops."""

__author__ = "730676554"


def w_sum(vals: list[float]) -> float:
    """Returns sum of all elements."""
    count: int = 0
    sum: float = 0
    while count < len(vals):
        sum = sum + vals[count]
        count = count + 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns sum of all elements using for...in."""
    sum: float = 0
    for elem in vals:
        sum = sum + elem
    return sum


def f_range_sum(vals: list[float]) -> float: 
    """Returns sum of all elements using for in range."""
    sum: float = 0
    for idx in range(0, len(vals)): 
        sum = sum + vals[idx]
    return sum