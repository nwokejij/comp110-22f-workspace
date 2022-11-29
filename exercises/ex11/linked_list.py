"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730555056"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns 'head.data' stored at the given index."""
    if head is None:
        return index
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Returns the highest value for head.data in a linked list."""
    highest: int
    if head is None:
        raise ValueError("Cannot call max with None.")
    else:
        if head.next is None:
            return head.data
        else:
            highest = head.data
            data: int = max(head.next)
            if highest < data:
                highest = data
            return highest


def linkify(items: list[int]) -> Optional[Node]:
    """Returns the Node representation of a given list."""
    if len(items) == 0:
        return None
    result: Node
    if len(items) == 1:
        result = Node(items[0], None)
        return result
    else:
        result = Node(items.pop(0), linkify(items))
    return result


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Scale a Node by a factor."""
    if head is None:
        return None
    result: Node
    if head.next is None:
        return Node(head.data * factor, None)
    else:
        result = Node(head.data * factor, scale(head.next, factor))
    return result