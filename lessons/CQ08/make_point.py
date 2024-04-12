"""Tests point.py file."""

__author__ = "730676554"

from point import Point

lit: Point = Point(1.0, 3.0)
lit.scale_by(4)
print(lit)
print(lit.scale(3))