#!/usr/bin/python3
"""Solution to the N Queens problem."""
import sys


def solve_queens_problem(board_size):
    """Prints the solution in the required format."""

    def is_valid_position(pos, occupied_pos):
        """
        Checks if placing a queen at position (row, col) is safe.

        Args:
            solution (list): Current state of the board.
            row (int): Row index for the queen.
            col (int): Column index for the queen.

        Returns:
            bool: True if safe, False otherwise.
        """
        for i in range(len(occupied_pos)):
            if (
                occupied_pos[i] == pos or
                occupied_pos[i] - i == pos - len(occupied_pos) or
                occupied_pos[i] + i == pos + len(occupied_pos)
            ):
                return False
        return True

    def place_queens(board_size, index, occupied_pos, solutions):
        """
        Recursively tries to place queens and backtracks if needed.

        Args:
            board_size (int): Size of the board (N x N).
            row (int): Current row to place a queen.
            solution (list): Current state of the board.
            solutions (list): Accumulates all valid solutions.
        """
        if index == board_size:
            solutions.append(occupied_pos[:])
            return

        for i in range(board_size):
            if is_valid_position(i, occupied_pos):
                occupied_pos.append(i)
                place_queens(board_size, index + 1, occupied_pos, solutions)
                occupied_pos.pop()

    solutions = []
    place_queens(board_size, 0, [], solutions)
    return solutions


def main():
    """Entry point of the script."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize solution array and list for all solutions
    solutions = solve_queens_problem(board_size)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    main()
