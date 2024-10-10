#!/usr/bin/python3
"""A module for generating Pascal's Triangle"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to 'n' rows.

    Args:
        n (int): Number of rows of Pascal's Triangle to generate.

    Returns:
        List[List[int]]: A list of lists representing Pascal's Triangle.
        Each list represents a row in the triangle.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for row in range(1, n):
        # Get the previous row
        prev_row = triangle[row - 1]
        # Start each new row with 1
        new_row = [1]

        # Fill the middle values in the new row
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])
            # End each row with 1
            new_row.append(1)
            triangle.append(new_row)

    return triangle


def print_triangle(triangle):
    """
    Print Pascal's Triangle in a readable format.

    Args:
        triangle (List[List[int]]): Pascal's Triangle to print.
    """
    for row in triangle:
        print(row)


if __name__ == "__main__":
    n = 5  # Example for testing
    print_triangle(pascal_triangle(n))
