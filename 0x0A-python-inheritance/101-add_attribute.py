#!/usr/bin/python3
"""
This module defines a function that adds a new attribute to an object
if it's possible.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible

    Args:
        obj: the object to add the attribute to
        attr (str): the name of the attribute
        value: the value of the attribute

    Raises:
        TypeError: if the object can't have new attributes
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
