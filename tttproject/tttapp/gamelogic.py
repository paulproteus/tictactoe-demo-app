import re

# Note: Having thought about it, we can use the string representation of
# the board and store no state in a Board class. So we will use functions
# rather than class methods.

def board_is_valid(s):
    return (
        len(s) == 9 and
        re.match('^[ox ]+$', s)
    )
