#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    :param grid: List of list of integers where 0 represents water and 1 represents land.
    :return: Integer representing the perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Subtract 1 for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:  # Up
                    perimeter -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:  # Down
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:  # Right
                    perimeter -= 1

    return perimeter