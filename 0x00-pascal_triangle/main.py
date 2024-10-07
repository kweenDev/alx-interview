#!/usr/bin/python3
"""
This script imports the pascal_triangle function
and displays the generated Pascal's Triangle.
"""

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle


def print_triangle(triangle):
    """
    Print the triangle in a formatted way.

    Args:
        triangle (List[List[int]]): The Pascal's Triangle to print.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
