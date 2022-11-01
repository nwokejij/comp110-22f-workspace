"""Ex05 No help I guess."""
__author__ = "730555056"


def only_evens(some_list: list[int]) -> list[int]:
    """Return a list of evens from a given list."""
    i: int = 0
    evens_list: list[int] = []
    while i < len(some_list):
        if some_list[i] % 2 == 0:
            evens_list.append(some_list[i])
        i += 1
    return evens_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Add another list onto another list and return the list without modifying any of the lists."""
    combined: list[int] = []
    i: int = 0
    j: int = 0

    if first_list == [] or second_list == []:
        if first_list == [] and second_list == []:
            return []
        elif first_list == []:
            while i < len(second_list):
                combined.append(second_list[i])
                i += 1
            return combined
        else:
            while i < len(first_list):
                combined.append(first_list[i])
                i += 1
            return combined

    while i < len(first_list):
        combined.append(first_list[i])
        i += 1
    while j < len(second_list):
        combined.append(second_list[j])
        j += 1
    return combined


def sub(a_list: list[int], findex: int, lindex: int) -> list[int]:
    """Will return a subset from 'list' starting from the first index to the last index minus 1."""
    subset: list[int] = []
    if findex > lindex or findex == len(a_list) or a_list == []:
        return subset
    # variables to access the first and last index of returned list
    i: int = findex
    j: int = lindex - 1
    # subset of list to store elements from index i to j
    if i < 0:
        i = 0
    k: int = i
    if j > len(a_list) - 1:
        j = len(a_list) - 1
    while k <= j:
        subset.append(a_list[k])
        k += 1
    return subset