#!/usr/bin/python3
"""
This module defines a function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.

    Args:
        filename (str): the name of the file to read from

    Returns:
        object: the Python object represented by the JSON data in the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
