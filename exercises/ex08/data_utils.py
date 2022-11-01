"""Dictionary related utility functions."""

__author__ = "730555056"

# Define your functions below
from csv import DictReader
from io import TextIOWrapper


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle: TextIOWrapper = open(filename, "r", encoding="utf8")
    # Read that file
    csv_reader: DictReader[str] = DictReader(file_handle)
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close that file
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], select: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    result_col: list[str] = []
    for each in table:
        if select in each:
            result_col.append(each[select])
    return result_col


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into a dictionary of columns."""
    column: dict[str, list[str]] = {}
    for row in rows[0]:
        column[row] = column_values(rows, row)
    return column


def head(table: dict[str, list[str]], upto: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the ifrst N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if upto > len(table):
        for column in table:
            result[column] = table[column]
        return result
    for column in table:
        values: list[str] = []
        for i in range(upto):
            values.append(table[column][i])
        result[column] = values
    return result


def select(table: dict[str, list[str]], copy: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for each in copy:
        result[each] = table[each]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    combined1: dict[str, list[str]] = {}
    for column in table1:
        combined1[column] = table1[column]
    for column in table2:
        if column in combined1:
            for item in table2[column]:
                combined1[column].append(item)
        else:
            combined1[column] = table2[column]
    return combined1


def count(string_values: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value and each value is the number of times the value appeared in input list."""
    result: dict[str, int] = {}
    for i in string_values:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
        