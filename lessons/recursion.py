"""Writing a recursive function from standard definition."""

__author__ = "730676554"


def f(n: int, k: int) -> int:
    """Returns n * k."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)
    

print(f(2, 2))
print(f(3, 4))
print(f(5, 4))
