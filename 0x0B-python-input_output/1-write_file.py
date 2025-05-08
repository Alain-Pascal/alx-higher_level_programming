#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a str to a text file (UTF8) and returns the number of chars written

    Args:
        filename (str): the name of the file to write to.
        text (str): the str to write to the file

    Returns:
        int: the number of chars written to the file
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
