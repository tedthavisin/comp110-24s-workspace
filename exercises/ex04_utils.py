"""List Utility Functions."""

__author__ = "730676554"


def all(x: list[int], y: int) -> bool:
    """Checks if all the numbers are the same."""
    idx: int = 0
    if len(x) == 0:
        return False
    while idx < len(x):
        if x[idx] != y:
            return False
        idx += 1
    else:
        return True


def max(x: list[int]) -> int:
    """Given a list of ints, should return the largest."""
    idx: int = 0
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = int(x[0])
    while idx < len(x):
        current: int = int(x[idx])
        if current > max:
            max = current
        idx += 1
    return max


def is_equal(x: list[int], y: list[int]) -> bool:
    """Returns True if every element at every index is equal."""
    if len(x) != len(y):
        return False
    for idx in range(len(x)):
        if x[idx] != y[idx]:
            return False
    return True


def extend(x: list[int], y: list[int]) -> None:
    """Adds the second list to the first."""
    for item in y:
        x.append(item)