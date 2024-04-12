"""Functions that implement sorting algorithms."""

__author__ = "730676554"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    sort: int = 1
    while sort < len(x):
        unsort: int = sort - 1
        min_index: int = x[sort]
        while unsort >= 0 and min_index < x[unsort]:
            x[unsort + 1] = x[unsort]
            unsort -= 1
        x[unsort + 1] = min_index
        sort += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    counter: int = 0
    while counter < len(x):
        counter2: int = counter + 1
        min_position = counter
        min_index: int = x[counter]
        while counter2 < len(x):
            if x[counter2] < min_index:
                min_position = counter2
                min_index = x[counter2]
            counter2 += 1
        (x[counter], x[min_position]) = (x[min_position], x[counter])    
        counter += 1
    return None
    