#!/usr/bin/python3
"""
This module defines a function that returns an object (Python data structure)
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: the JSON str to be deserialized into Python obj

    Returns:
        object: the Python obj represented by the JSON str
    """

    return json.loads(my_str)
