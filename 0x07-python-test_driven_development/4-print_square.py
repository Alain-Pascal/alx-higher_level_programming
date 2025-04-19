#!/usr/bin/python3
"""
This  module defines a function that
prints a square with the char #.
"""


def print_square(size):
    """
    Prints a square with the char #

    Args:
        size (int): length of the square

    Raises:
        TypeError: If size is not an int
        ValueError: If size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
