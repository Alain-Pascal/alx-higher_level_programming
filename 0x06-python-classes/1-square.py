#!/usr/bin/python3
"""Square module
This module contains a class that defines a square
and initializes it with a size
"""


class Square:
    """Defines a square
    """

    def __init__(self, size):
        """Initialize Square objects

        Args:
            size: size of one edge of the square
        """
        self.__size = size
