"""List Utility Functions."""

__author__ = "730676554"


def all (x: list[int], y: int) -> bool:
    """Checks if all the numbers are the same."""
    for idx in x:
        if x[idx] != y:
            return False
    return True


def max(x: list[int]) -> int:
    """Given a list of ints, should return the largest."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = 0
    for idx in x:
        if x[idx] > max:
            x[idx] = max
    return max


def is_equal(x: list[int], y: list[int]) -> bool:
    """Returns True if every element at every index is equal."""
    for idx in x:
        if x[idx] != y[idx]:
            return False
    return True


def extend(x: list[int], y: list[int]) -> None:
    """Adds the second list to the first."""
    for item in y:
        x.append(item)

   