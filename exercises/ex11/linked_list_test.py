"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730555056"


# edge case
def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


# use case
def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


# edge case
def test_edge_value_at() -> None:
    """Should return the index if there is an empty Linked List."""
    assert value_at(None, 2) == 2


# use case
def test_use_value_at() -> None:
    """Should return the 'head.data' for a given index if Linked List is not ordered numerically."""
    assert value_at(Node(40, Node(90, Node(50, None))), 2) == 50


# edge case
def test_edge_max() -> None:
    """Should raise a ValueError for an empty Linked List."""
    with pytest.raises(ValueError):
        max(None)


# use case
def test_use_max() -> None:
    """Returns the highest data of a Linked List of Nodes."""
    assert max(Node(30, Node(90, Node(100, None)))) == 100


# edge case
def test_edge_linkify() -> None:
    """If only one element in 'items', should return 'element -> None'."""
    assert str(linkify([2])) == "2 -> None"


# use case
def test_use_linkify() -> None:
    """Should link elements in a list[int] in a Linked List, regardless of repetitions."""
    assert str(linkify([2, 2, 2, 3])) == "2 -> 2 -> 2 -> 3 -> None"


# edge case
def test_edge_scale() -> None:
    """Should work for negative factors."""
    assert str(scale(linkify([1, 2, 3]), -1)) == "-1 -> -2 -> -3 -> None"


# use case
def test_use_scale() -> None:
    """Should scale a Linked List by a given factor."""
    assert str(scale(linkify([2, 2, 3]), 5)) == "10 -> 10 -> 15 -> None"