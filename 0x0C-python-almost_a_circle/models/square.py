#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance

        Args:
            size (int): the size of the square (width and height)
            x (int): x-coordinate of the square
            y (int): y-coordinate of the square
            id (int): the id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        Args:
            value (int): the size to set
                (applies to both width and height)
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes of the Square instance

        Args:
            *args: variable number of arguments
            **kwargs: ky-value pairs of attributes to update
        """
        if args and len(args) > 0:
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
