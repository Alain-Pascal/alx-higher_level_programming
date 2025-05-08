#!/usr/bin/python3
"""
This module defines a function that reads a text file (UTF8)
and prints it to stdout.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
    # The end="" argument prevents print from adding an extra newline
    # at the end of the output, which is the default behavior of print.
