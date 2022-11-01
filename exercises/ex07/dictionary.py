"""Exercise 7: Dictionaries."""
__author__ = "730555056"


def invert(invert_this: dict[str, str]) -> dict[str, str]:
    """Reverses the keys and values in a dict."""
    new_dict: dict[str, str] = dict()
    values_list: list[str] = []
    for x in invert_this:
        values_list.append(invert_this[x])
    i: int = 0
    j: int = i + 1
    while i < len(values_list):
        while j < len(values_list):
            if values_list[i] == values_list[j]:
                raise KeyError("KeyError: Cannot have two keys equal to each other.")
            j += 1
        i += 1
        j = i + 1
    for key in invert_this:
        new_dict[invert_this[key]] = key
    return new_dict


def favorite_color(color: dict[str, str]) -> str:
    """Returns color that appears the most."""
    color_values: list[str] = []
    single_color_values: list[str] = []
    most_rep: str = ""
    count_rep: int = 0
    max_rep: int = 0
    i: int = 0
    for x in color:
        color_values.append(color[x])
        if color[x] not in single_color_values:
            single_color_values.append(color[x])
    for single1 in single_color_values:
        for single2 in color_values:
            if single1 == single2:
                count_rep += 1
            
        if max_rep < count_rep:
            max_rep = count_rep
            most_rep = single1
        count_rep = 0
    return most_rep


def count(passed: list[str]) -> dict[str, int]:
    """Returns a dictionary with the number of times a string appears in the input list."""
    result: dict[str, int] = dict()
    for e_string in passed:
        if e_string in result:
            result[e_string] += 1
        else:
            result[e_string] = 1
    return result