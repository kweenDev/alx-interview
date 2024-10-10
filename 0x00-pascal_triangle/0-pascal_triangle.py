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
    # This will hold the entire Pascal's Triangle
    res = []

    if n > 0:
        # Iterate through each row, starting from 1 up to n
        for i in range(1, n + 1):
            # List to hold the values for the current row
            level = []
            # This is the binomial coefficient starting at 1
            C = 1

            # Iterate through each position in the current row
            for j in range(1, i + 1):
                level.append(C)  # Append the current value of C to the row
                # Update C using the formula C = C * (i - j) // j for binomial coefficients
                C = C * (i - j) // j

            # Add the completed row to the triangle
            res.append(level)

    return res  # Return the full Pascal's Triangle


def print_triangle(triangle):
    """
    Print Pascal's Triangle in a readable format.

    Args:
        triangle (List[List[int]]): Pascal's Triangle to print.
    """
    for row in triangle:
        print(row)  # Print each row of the triangle


if __name__ == "__main__":
    n = 5  # Example for testing
    print_triangle(pascal_triangle(n))
