"""Utility functions for working with Linked Lists."""
 
from __future__ import annotations
 
__author__ = "730676554"
 
 
class Node:
    """An item in a singly-linked list."""
    data: int
    next: Node | None
 
    def __init__(self, data: int, next: Node | None):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return the data attribute for the first element in the linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return a linked list of every element minus the head."""
        if self.next is None:
            return None
        else:
            return self.next
        
    def last(self) -> int:
        """Returns the data of the last element in the linked list."""
        if self.next is None:
            return self.data
        else:
            return self.next.last()  

        
# 3 -> 4 -> 5 -> None

c: Node = Node(5, None)
b: Node = Node(4, c)
a: Node = Node(3, b)       

node_c: Node = Node(2, None)
node_b: Node = Node(1, node_c)
node_a: Node = Node(0, node_b)

# print(node_a.head())
# print(node_a.tail())
# print(node_a.last())


def value_at(head: Node | None, index: int) -> int:
    """Returns value at index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns max data."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    max_data: int = head.data
    current_node: Node | None = head.next

    while current_node is not None:
        if current_node.data > max_data:
            max_data = current_node.data
        current_node = current_node.next
    return max_data

# print(max(Node(10, Node(20, Node(30, None)))))


def linkify(items: list[int]) -> Node | None:
    """Returns linked list of Nodes."""
    if len(items) == 0:
        return None

    head = Node(items[0], None)
    current_node = head

    for item in items[1:]:
        new_node = Node(item, None)
        current_node.next = new_node
        current_node = new_node

    return head


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list of Nodes where each value is multiplied by the factor."""
    if head is None:
        return None
    
    new_head = Node(head.data * factor, None)
    current_node = new_head
    original_node = head.next

    while original_node is not None:
        new_node = Node(original_node.data * factor, None)
        current_node.next = new_node
        current_node = new_node
        original_node = original_node.next

    return new_head


print(scale(linkify([1, 2, 3]), 2))