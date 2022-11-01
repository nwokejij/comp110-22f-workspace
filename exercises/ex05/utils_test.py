"""Utils test file."""
__author__ = "730555056"


from utils import only_evens, concat, sub

"""Testing only_evens."""


# edge case
def test_only_evens_empty() -> None:
    """Should return an empty list if argument passed is an empty list."""
    assert only_evens([]) == []


def test_only_evens_use_case1() -> None:
    """Testing use case 1 (evens and odds)."""
    assert only_evens([1, 3, 5, 6, 18]) == [6, 18]


# use case 2
def test_only_evens_use_case2() -> None:
    """Testing second use case (no evens)."""
    assert only_evens([5, 15, 19, 35, 41, 101]) == []


"""Testing concat."""


# edge case
def test_concat_edge() -> None:
    """If user passes an empty list, the list that is not empty should be returned."""
    assert concat([2], []) == [2]


# use case
def test_concat_use_case1() -> None:
    """Testing first use case (same length)."""
    assert concat([1], [2]) == [1, 2]


# use case 2
def test_concat_use_case2() -> None:
    """Testing second use case (different lengths)."""
    assert concat([2, 4, 5, 6], [3, 4, 5]) == [2, 4, 5, 6, 3, 4, 5]


def test_concat_first_empty() -> None:
    """Testing one single list and one empty list."""
    assert concat([1], []) == [1]


"""Testing sub."""


# edge case
def test_sub_edge() -> None:
    """If user passes a start index that is equal to end index, should return an empty list."""
    assert sub([3, 5, 6, 9], 3, 3) == []


def test_sub_greater() -> None:
    """If end index is greater than length of list."""
    assert sub([3, 5, 6, 9], 1, 10000) == [5, 6, 9]


def test_sub_negative_start() -> None:
    """If start index is negative, start index is reassigned from the beginning of the list."""
    assert sub([3, 5, 6, 9], -21, 10000) == [3, 5, 6, 9]


# use case
def test_sub_case1() -> None:
    """Testing first use case (adjacent indices)."""
    assert sub([3, 5, 6, 9, 1], 3, 4) == [9]


# use case 2
def test_sub_case2() -> None:
    """Testing second use case (start and end indices fall within range)."""
    assert sub([3, 2, 15, 5, 19], 1, 4) == [2, 15, 5]