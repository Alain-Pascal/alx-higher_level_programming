#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance of a
class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or an inherited class,
        False otherwise.
    """
    if type(obj) is a_class:
        return False  # Exclude direct instances of a_class
    return isinstance(obj, a_class)
