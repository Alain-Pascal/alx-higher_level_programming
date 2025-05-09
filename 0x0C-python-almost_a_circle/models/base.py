#!/usr/bin/python3
"""
Defines a base class for all other classes in the project.
"""


class Base:
    """
    Base class to manage the id attribute for all future classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance

        Args:
            id (int): The id of the instance. If None, the id is set to
            the next available id.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
