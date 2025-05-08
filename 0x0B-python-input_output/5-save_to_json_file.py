#!/usr/bin/python3
"""
This module defines a function that writes an Object to a file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an obj to a file, using a JSON representation.

    Args:
        my_obj: the Python obj to be serialized and save to the file
        filename (str): the name of the file to write to
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
