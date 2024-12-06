#!/usr/bin/python3
"""
Solution to the N Queens problem.
"""

import sys


def printSolution(solution):
    """Prints the solution in the required format."""
    print([[row, col] for row, col in enumerate(solution)])


def isSafe(solution, row, col):
    """
    Checks if placing a queen at position (row, col) is safe.
    """
    for i in range(row):
        # Check column and diagonal clashes
        if solution[i] == col or abs(solution[i] - col) == abs(i - row):
            return False
    return True


def solveNQueens(n, row, solution):
    """
    Recursively tries to place queens and backtracks if needed.
    """
    if row == n:
        printSolution(solution)
        return

    for col in range(n):
        if isSafe(solution, row, col):
            solution[row] = col
            solveNQueens(n, row + 1, solution)
            # Backtrack (implicitly handled by overwriting `solution[row]`)


def main():
    """Entry point of the script."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize solution array
    solution = [-1] * n
    solveNQueens(n, 0, solution)


if __name__ == "__main__":
    main()
