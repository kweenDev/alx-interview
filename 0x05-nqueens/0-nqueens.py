#!/usr/bin/python3
"""
Solution to the N Queens problem.
"""

import sys


def printSolution(solution):
    """Prints the solution in the required format.

    Args:
        solution (list): List where the index represents the row, and the value represents the column of a queen.
    """
    print([[row, col] for row, col in enumerate(solution)])


def isSafe(solution, row, col):
    """
    Checks if placing a queen at position (row, col) is safe.

    Args:
        solution (list): Current state of the board.
        row (int): Row index for the queen.
        col (int): Column index for the queen.

    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(row):
        # Check column and diagonal clashes
        if solution[i] == col or abs(solution[i] - col) == abs(i - row):
            return False
    return True


def solveNQueens(n, row, solution, solutions):
    """
    Recursively tries to place queens and backtracks if needed.

    Args:
        n (int): Size of the board (N x N).
        row (int): Current row to place a queen.
        solution (list): Current state of the board.
        solutions (list): Accumulates all valid solutions.
    """
    if row == n:
        solutions.append(solution[:])
        return

    for col in range(n):
        if isSafe(solution, row, col):
            solution[row] = col
            solveNQueens(n, row + 1, solution, solutions)
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

    # Initialize solution array and list for all solutions
    solution = [-1] * n
    solutions = []
    solveNQueens(n, 0, solution, solutions)

    for solution in solutions:
        printSolution(solution)


if __name__ == "__main__":
    main()
