#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """
    A class that represents the base geometry.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
