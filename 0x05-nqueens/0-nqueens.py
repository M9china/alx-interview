#!/usr/bin/python3

import sys


"""
This module solves the N-Queens puzzle.

"""


def is_safe(board, row, col):
    """Check if it's safe to place a queen at (row, col)."""
    for r in range(row):
        # Check if the column is safe
        if board[r] == col:
            return False
        # Check diagonals
        if abs(board[r] - col) == row - r:
            return False
    return True


def solve_nqueens(N, board, row, solutions):
    """Recursively solve the N-Queens problem."""
    if row == N:
        # Add the solution in the correct format, each queen as [row, col]
        solutions.append([[r, board[r]] for r in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1, solutions)


def nqueens(N):
    """Main function to solve the N-Queens problem."""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N  # Initialize the board with -1 (no queens placed)
    solutions = []  # List to store the solutions
    solve_nqueens(N, board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
