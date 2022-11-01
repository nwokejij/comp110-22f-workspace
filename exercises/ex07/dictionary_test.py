"""Dictionary Test."""
__author__ = "730555056"

from dictionary import invert, favorite_color, count

"""Testing invert."""


# edge case
def test_edge_case_invert() -> None:
    """Should return an empty dictionary if there invert() passes an empty dictionary."""
    assert invert({}) == {}


def test_use_case_1invert() -> None:
    """Should return reversed key-values pairs for characters."""
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


def test_use_case_2invert() -> None:
    """Should return reversed key-values for strings."""
    assert invert({"jack": "bill", "dill": "quill"}) == {"bill": "jack", "quill": "dill"}


def test_edge_case_favorite_color() -> None:
    """Should return empty string if empty dictionary."""
    assert favorite_color({}) == ""


def test_use_case_1favorite_color() -> None:
    """Should return color that appears the most."""
    assert favorite_color({"Jim": "blue", "Jack": "blue", "Jeffery": "blue", "Jessie": "yellow", "Jimson": "red", "Jimmy": "green"}) == "blue"


def test_use_case_2favorite_color() -> None:
    """If colors appear same amount of times, should display color that came first in the dictionary."""
    assert favorite_color({"Jeff": "red", "Jim": "blue"}) == "red"


def test_edge_case_count() -> None:
    """Should return an empty dictionary if an empty dictionary is passed."""
    assert count([]) == {}


def test_use_case_1count() -> None:
    """Should return number of times a string appears in a list it appears multiple times."""
    assert count(["fish", "fish", "fish", "fish"]) == {"fish": 4}


def test_use_case_2count() -> None:
    """Should assert number of times each string appears in a list if they each appear once."""
    assert count(["Gumbo", "Jumbo", "Bamba"]) == {"Gumbo": 1, "Jumbo": 1, "Bamba": 1}