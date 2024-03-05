"""Splitting a dictionary into two lists."""

__author__ = "730676554"


def get_keys(x: dict[str, int]) -> list[str]:
    """Get keys."""
    new_list: list[str] = []
    for key in x:
        new_list.append(key)
    return new_list


def get_values(x: dict[str, int]) -> list[int]:
    """Returns values using key."""
    new_list: list[int] = []
    for key in x:
        new_list.append(x[key])
    return new_list