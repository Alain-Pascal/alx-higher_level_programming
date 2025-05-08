#!/usr/bin/python3
"""
This module defines a function that appends a string at
the end of a text file (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a str at the end of a text file (UTF8) and
    returns the number of chars added

    Args:
        filename (str): the name of the file to append to.
        text (str): the str to append to the file

    Returns:
        int: the number of chars added to the file
    """

    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
