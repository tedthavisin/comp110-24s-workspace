"""File to define Bear class."""

__author__ = "730676554"


class Bear:
    """Bear object has age and hunger attributes."""
    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Creates a bear object."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self) -> None:
        """Passes one day for the bear."""
        self.age = self.age + 1
        self.hunger_score = self.hunger_score - 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """The bear eats a number of fish and adds to hunger."""
        self.hunger_score = self.hunger_score + num_fish
        return None