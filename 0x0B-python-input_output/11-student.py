#!/usr/bin/python3
"""
This module defines a Student class.
"""


class Student:
    """ Defines a student """

    def __init__(self, first_name, last_name, age):
        """ Initializes the student
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): List of attributes to retrieve

        Returns:
            dict: Dictionary representation of the student
        """
        if attrs is None:
            return {
                'last_name': self.last_name,
                'first_name': self.first_name,
                'age': self.age
            }
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json_data):
        """
        Replaces all attributes of the Student instance

        Args:
            json_data (dict): Dictionary with new attribute values
        """
        for key, value in json_data.items():
            setattr(self, key, value)
