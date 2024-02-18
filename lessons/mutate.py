"""Mutating functions."""

__author__ = "730676554"


def manual_append(x: list[int], y: int) -> None:   
    """Adds the y variable onto the list x."""
    x.append(y)    


def double(x: list[int]) -> None:
    """Multiplies each number in x list by 2."""
    count: int = 0
    while count < len(x):
        x[count] = x[count] * 2
        count = count + 1