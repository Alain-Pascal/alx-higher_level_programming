#!/usr/bin/python3

"""
This module defines a Rectangle class with width, height,
area, perimeter, customizable string representation,
object deletion handling, instance counting,
a static method for comparing rectangles,
and a class method for creating squares.
"""


class Rectangle:
    """
    A class that defines a rectangle with width and height, and can calculate
    its area, perimeter, provide string and evaluable representations,
    handle object deletion, count instances, compare rectangles,
    and create squares.
    """

    number_of_instances = 0  # Public class attribute to count instances
    print_symbol = "#"  # Public class attribute for the print symbol

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with optional width and height.
        Increments the number_of_instances class attribute.

        Args:
            width (int, optional): width of the rectangle
            height (int, optional): height of the rectangle
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1  # Increment on instantiation

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

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: the area of the rectangle (width * height)
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
            int: the perimeter of the rectangle
                (2 * (width + height))
            0: if either width or height is 0
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        using the '#' character

        Returns:
            str: string representing the rectangle
                using the '#' char
            empty str: if either width or height is 0
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join(
            str(
                Rectangle.print_symbol
                ) * self.__width for _ in range(self.__height)
            )

    def __repr__(self):
        """
        Returns a string representation
        of the rectangle object that can be used
        to recreate the object using eval()
        """

        return "Rectangle({}, {})".format(
            self.__width,
            self.__height
            )

    def __del__(self):
        """
        Prints Bye message when an instance of Rectangle is deleted
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement on deletion

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): first rectangle to compare
            rect_2 (Rectangle): second rectangle to compare

        Raises:
            TypeError: if either rect_1
                or rect_2 is not an instance of Rectangle

        Returns:
            Rectangle: the rectangle with the larger area,
                or rect_1 if both have the same area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance
        with width == height == size

        Args:
            size (int): size of the square. Defaults to 0

        Returns:
            Rectangle: new Rectangle instance representing a square
        """

        return cls(size, size)
