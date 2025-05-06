#!/usr/bin/python3
"""
This function returns the list of available attributes and
methods of an object.
"""


def lookup(obj):
    """
    Returns a list of objects containing the names of attributes
    and methods of the given object.

    Args:
        obj: The object whose attributes and methods are to be listed.

    Returns:
        list: A list of strings representing the names of attributes
              and methods of the object.
    """
    return dir(obj)
