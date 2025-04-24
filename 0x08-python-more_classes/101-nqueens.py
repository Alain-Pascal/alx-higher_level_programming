#!/usr/bin/python3

""" Solve the N queens problem """


def is_safe(board, row, col):
    """
    Checks if a queen can be placed at board[row][col]

    Args:
        board (list of lists): the current board configuration
        row (int): the row to check
        col (int): the column to check

    Returns:
        bool: True if the position is safe, False otherwise
    """

    # check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col):
    """
    Recursively solves the N queens problem using backtracking

    Args:
        board (list of lists): the board configuration
        col (int): the current column being considered

    Returns:
        bool: True if a solution is found, False otherwise
    """

    if col >= len(board):
        return True

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_nqueens(board, col + 1):
                return True

            board[row][col] = 0  # Backtrack

        return False


def solve_n_queens(n):
    """
    Solves the N queens problem for a given N.

    Args:
        n (int): the size of the board (N x N)
    """

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve_nqueens_util(board, col):
        """ Recursive utility function to find all solutions"""
        if col >= n:
            solutions.append([
                [r, c] for r, row in enumerate(
                    board
                    ) for c, val in enumerate(
                    row
                    ) if val == 1
                ])
            return

        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve_nqueens_util(board, col + 1)
                board[row][col] = 0  # Backtrack

    solve_nqueens_util(board, 0)
    for solution in solutions:
        print(solution)


def print_usage():
    """ Prints the usage message and exits"""
    print("Usage: nqueens N")
    exit(1)


def print_error(message):
    """ Prints an message and exits"""
    print(message)
    exit(1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print_usage()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_error("N must be a number")

    if n < 4:
        print_error("N must be at least 4")

    solve_n_queens(n)
