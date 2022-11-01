"""Example implementing a list utility function"""

# Function name: contains
# We will have 2 parameters: needle(str, haystack (list[str]))
# Return type bool
# Gameplan:
# 1. Start with the first index
# 2. Loop through every index
#    2.A Test if item at index equal to needle
#      2. A True Return True! We found it!


def contains(needle: str, haystack: list[str]) -> bool:
    """"""
    i: int = 0
    while i < len(haystack):
        if needle == haystack[i]:
            return True
        i += 1

    
    return False