"""Mutating functions."""

__author__ = 730676554

#x is the list and y is the number being added.
def manual_append(x: list[int], y: int):
    x.append(y)

#Test
a: list[int] = [1,2,3]
manual_append(a,2)
print(a)

#x is the name of the list.
def double(x: list[int]):
    count: int = 0
    #acts as an index and keeps count of everytime it loops.
    while count < len(x):
        x[count] = x[count] * 2
        count = count + 1

#Test
b: list[int] = [4,2,10]
double(b)
print(b)