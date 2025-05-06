#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square and inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size  # Store size as a private attribute
        super().__init__(size, size)  # Call the parent constructor

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2  # Area of a square is size^2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representing the square.
        """
        # Change the self.width or sel.height to self.__size
        return "[Square] {}/{}".format(self.__size, self.__size)
