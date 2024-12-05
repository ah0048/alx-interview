#!/usr/bin/python3
'''function module'''


def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''

    if len(grid) > 100 or len(grid[0]) > 100:
        return "grid width and height must not exceed 100"

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:

                if i > 0 and grid[i - 1][j] == 0:
                    perimeter += 1
                if i + 1 != len(grid) and grid[i + 1][j] == 0:
                    perimeter += 1
                if j + 1 != len(grid[i]) and grid[i][j + 1] == 0:
                    perimeter += 1
                if j > 0 and grid[i][j - 1] == 0:
                    perimeter += 1

    return perimeter
