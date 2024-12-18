#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid.

    Args:
    grid (list of list of int): 2D array representing the island grid.
        - 1 represents land.
        - 0 represents water.

    Returns:
    int: The perimeter of the island.

    The function calculates the perimeter of the island described in the grid.
    The island is represented by 1s (land) and 0s (water). The perimeter
    is calculated based on the number of edges of land cells exposed to
    water or grid boundaries.
    """
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:  # Found land
                # Check each of the 4 neighbors (up, down, left, right)
                # and count edges exposed to water (or out of bounds)
                if i == 0 or grid[i-1][j] == 0:  # Up
                    perimeter += 1
                if i == len(grid) - 1 or grid[i+1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1

    return perimeter
