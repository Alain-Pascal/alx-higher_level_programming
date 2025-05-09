#!/usr/bin/python3
"""
Defines a base class for all other classes in the project.
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON str representation of a list of dicts

        Args:
            list_dictionaries (list): list of dicts

        Returns:
            str: the JSON str representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
