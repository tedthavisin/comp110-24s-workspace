"""My first program for COMP110."""

__author__ = "730676554"
print("Hello, world.")

def main_planner(guests: int) -> None:
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(guests)))

def tea_bags(people: int) -> int:
    return people * 2

main_planner(3)