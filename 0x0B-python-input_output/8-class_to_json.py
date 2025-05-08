#!/usr/bin/python3
"""
This module defines a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: The object to serialize.

    Returns:
        dict: The dictionary description of the object.
    """
    return {
        attr: getattr(obj, attr)
        for attr in dir(obj)
        if not attr.startswith('__') and not callable(getattr(obj, attr))
    }
