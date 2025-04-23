#!/usr/bin/python3

"""
This module defines a Rectangle class
with width and height attributes
"""


class Rectangle:
    """
    A class that defines a rectangle
    with width and height
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object
        with optional width and height

        Args:
            width (int, optional): width of the rectangle
            height (int, optional): height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle

        Returns:
            int: width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): width value to set

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle

        Returns:
            int: height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value (int): height value to set

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
