#!/usr/bin/env python3
"""
Author: Brandon O'Briant
Date: 2022.02.02
Purpose: Solve any 9x9 Soduku Puzzel given an input string from user.
"""

from utils import display_grid, instructions, get_grid


ROW = 'ABCDEFGHI'
COL = '123456789'
EXAMPLE_GRID = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'


if __name__ == '__main__':
    instructions(EXAMPLE_GRID, ROW, COL)
    print("\n\n")
    grid = get_grid()
    display_grid(grid, ROW, COL)
