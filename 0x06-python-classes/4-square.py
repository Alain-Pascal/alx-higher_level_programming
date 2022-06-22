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
        self.size = size

    def area(self):
        """Public instance method

        Returns:
            the current square area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Getter method that retrieves the size of square

        Returns:
            size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Seeter method that sets size of square to a value

        Args:
            value (int): value to set as size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
