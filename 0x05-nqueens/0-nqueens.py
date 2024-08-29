#!/usr/bin/python3
"""
This module solves the N-Queens problem using a backtracking algorithm.
"""
import sys


def is_safe(board, row, col):
    """
    Check if placing a queen at (row, col) is safe.
    Returns:
    - bool: True if safe, else False.
    """
    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """
    Use backtracking to find all solutions for N-Queens.
    """
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)


def nqueens(N):
    """
    Validate input and solve the N-Queens problem.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * N
    solve_nqueens(N, 0, board, solutions)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if __name__ == "__main__":
    """
    Entry point.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
