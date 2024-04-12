"""CQ08 Practice with OOP."""

from __future__ import annotations

__author__ = "730676554"


class Point:
    """Has two attributes x and y."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Creates a new Point object."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates by a constant factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Returns a new Point with x and y attributes equal to the x & y multipled by the factor."""
        new: Point = Point(self.x * factor, self.y * factor)
        return new
    