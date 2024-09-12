"""File to define Fish class."""

__author__ = "730676554"


class Fish:
    """Fish object has age attribute."""
    age: int

    def __init__(self) -> None:
        """Creates a fish object."""
        self.age = 0
        return None
    
    def one_day(self) -> None:
        """Passes one day for the fish object."""
        self.age += 1
        return None