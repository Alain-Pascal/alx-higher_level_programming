#!/usr/bin/python3
"""
This module defines a function that returns the JSON representation
of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an obj (str)

    Args:
        my_obj: python obj to be serialized into JSON str

    Returns:
        str: the JSON str representation of the obj
    """

    return json.dumps(my_obj)
