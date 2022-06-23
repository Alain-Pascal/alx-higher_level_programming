#!/usr/bin/python3
"""Square module
This module contains a class that defines a square
and initializes it with a size
"""


class Square:
    """Defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square objects

        Args:
            size (int): size of the square
            position (int, int): coordinates of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """Public instance method

        Returns:
            the current square area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter method that retrieves the size of square

        Returns:
            size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method that sets size of square to a value

        Args:
            value (int): value to set as size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve position of square

        Returns:
            position of square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter method that sets the position of the square
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints in stdout the square with the character #
        """
        if (self.__size == 0):
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print("")
