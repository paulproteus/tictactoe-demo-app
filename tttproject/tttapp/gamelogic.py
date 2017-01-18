import re

# Note: Having thought about it, we can use the string representation of
# the board and store no state in a Board class. So we will use functions
# rather than class methods.
#
# This has the upside that we can't write mutability problems into
# this codebase.

def string_as_rows(s):
    return s[:3], s[3:6], s[6:]

def board_is_valid(s):
    return (
        len(s) == 9 and
        re.match('^[ox ]+$', s)
    )

def get_shallow_value(s):
    '''Return 1 if player "o" is the winner.

    Return 0 if player "x" is the winner.

    Return None if there is no winner yet.

    The function is called shallow value because it does no tree traversal.'''
    rows = string_as_rows(s)
    # TODO: Refactor so that I don't hard-code 'x' and 'o' quite so much.
    # Check for row win condition
    if 'ooo' in rows:
        return 1
    if 'xxx' in rows:
        return 0

    # Check for columns win condition
    for i in range(3):
        if (rows[0][i] == 'o' and
            rows[1][i] == 'o' and
            rows[2][i] == 'o'):
            return 1
        if (rows[0][i] == 'x' and
            rows[1][i] == 'x' and
            rows[2][i] == 'x'):
            return 0

    # Check for diagonal win conditions.
    if (rows[0][0] == 'o' and
        rows[1][1] == 'o' and
        rows[2][2] == 'o'):
        return 1
    if (rows[0][0] == 'x' and
        rows[1][1] == 'x' and
        rows[2][2] == 'x'):
        return 0
    if (rows[2][0] == 'o' and
        rows[1][1] == 'o' and
        rows[0][2] == 'o'):
        return 1
    if (rows[2][0] == 'x' and
        rows[1][1] == 'x' and
        rows[0][2] == 'x'):
        return 0

    return None
