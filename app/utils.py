"""
this contains the utility functions for you to run your model.
You should have already found the optimum confidence-level
for your model to have the best balance between precision and recall.
"""
import re


def cross(rows, cols):
    """Given two strings, a and b, concatenate letter in string a
    with letter in string b to create a label for each box in the
    Soduku puzzel grid.

    Args:
        rows - str: alphabet label for box (i.e. side label) for a given row
        cols - str: numeric label for box (i.e. top label) for a given column

    Returns:
        list of all possible comibnations of letters from string a and string b
    """
    return [row_label+col_label for row_label in rows for col_label in cols]


def row_units(rows, cols):
    """Create row units.

    Args:
        rows (list): rows label for board.
        cols (list): cols label for board.
    Returns:
        row_unit (list): row unit label for board.
    """
    return [cross(r, cols) for r in rows]


def col_units(rows, cols):
    """Create column units for board

    Args:
        rows (list): rows label for board.
        cols (list): cols label for board.
    Returns:
        col_unit - list: column unit label for board.
    """
    return [cross(rows, c) for c in cols]


def square_units(rows, cols):
    """Create square units for board i.e. (row, col) unit

    Args:
        rows (list): rows label for board.
        cols (list): cols label for board.
    Returns:
        squre_unit - list: square unit label for board.
    """
    square_unit = [cross(row_s, col_s)
                   for row_s in (rows[0:3], rows[3:6], rows[6:9])
                   for col_s in (cols[0:3], cols[3:6], cols[6:6])]
    return square_unit


def unit_list(rows, cols):
    """Create list of board units.

    Args:
       rows_units (list): list of row units
       col_units (list): list of column units
       square_units (list): list of (row, col) units
    Returns:
       square_units (list): concatenated row_units, col_units, squre_units
    """
    unitlist = row_units(rows, cols) + \
        col_units(rows, cols) + \
        square_units(rows, cols)
    return unitlist


def boxes(row, cols):
    """Create boxes (row, col)

    Args:
        row (list): list of column elements
        col (list): list of column elements
    Returns:
        boxlst (list): list of box elements i.e. ['A1', 'A2', ..., 'I8', 'I9']
    """
    return cross(row, cols)


def peers(units, boxes_lst):
    """Convert untis and boxes lists into {<unit>, <peer values>} dict.

    Args:
        units:
        boxes:
    Returns:
        dictionary of peers
        - keys: box label (square in board)
        - values: peers to the square in the board
    """
    return dict((s, set(sum([units[s], []])) - set([s])) for s in boxes_lst)


def grid_values(row, col, grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
        row (list):
        col (list):
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    return dict(zip(boxes(row, col), grid))


def display_grid(grid, rows, cols):
    """Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    values = grid_values(rows, cols, grid)
    width = 1+max(len(values[square]) for square in boxes(rows, cols))
    line = '+'.join(['-'*(width*3)]*3)
    for row in rows:
        print(''.join(values[row+col].center(width)+('|' if col in '36' else '') for col in cols))
        if row in 'CF':
            print(line)


def greeting():
    """Great User to Program"""
    return print("Hello! Welcome to Soduku Solver!")


def instructions(values, row, col):
    """Provides instructions for users input."""
    print("Please provide a Soduku Puzzel grid in the following format:\n")
    print("'..3.2.6..9..3.5..1..18.64....81.19..7......8..67.82....26.95..8..2.3..9..5.1.3..")
    print("Where '.' is the blank square in puzzle and the '1-9' value is the given")
    print("See example board below which corresponds to the example grid input above.")
    return display_grid(values, row, col)


def get_grid():
    """Get grid from user input"""
    while True:
        grid = "'"+input("Enter grid: ")+"'"
        match = re.match(r"(^[0-9\.]*$)", grid)
        try:
            if match and len(grid) == 81:
                break
        except ValueError:
            print("Grid must only be '.' for blanks and '1-9' for given values.")
            continue
        return grid
