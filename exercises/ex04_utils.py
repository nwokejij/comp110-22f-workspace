"""Experimenting with Lists."""
__author__ = "730555056"


def all(integer_list: list[int], integer: int) -> bool:
    """Returns False if all integers in integer_list does not equal integer, True otherwise."""
    if len(integer_list) == 0:
        return False
    i: int = 0
    while (i < len(integer_list)):
        if integer_list[i] != integer:
            return False
        i += 1
    return True


def max(integer_list: list[int]) -> int:
    """Return the greatest value in a list, if the list is empty raise a ValueError."""
    j: int = 1
    if (len(integer_list) > 0):
        max = integer_list[0]
        while (j < len(integer_list)):
            if max < integer_list[j]:
                max = integer_list[j]
            j += 1
        return max
    else:
        raise ValueError("max() arg is an empty List")


def is_equal(f_list: list[int], s_list: list[int]) -> bool:
    """Given two integer lists, returns True if each element of first_list is identical to each element of second_list, False otherwise."""
    if len(f_list) != len(s_list):
        return False
    else:
        i: int = 0
        while i < len(f_list):
            if f_list[i] != s_list[i]:
                return False
            i += 1
        return True
    
    
