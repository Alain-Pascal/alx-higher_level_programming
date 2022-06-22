#!/usr/bin/python3
"""Square module
This module contains a class that defines a square
and initializes it with a size
"""


class Square:
    """Defines a square
    """

    def __init__(self, size=0):
        """Initialize Square objects

        Args:
            size (int): size of one edge of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method

        Returns:
            the current square area
        """
        return (self.__size ** 2)
