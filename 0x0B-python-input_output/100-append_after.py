#!/usr/bin/python3
"""
This module defines a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific str

    Args:
        filename (str): the name of the file
        search_string (str): the str to search for in each file
        new_string (str): the str to insert after each matching line
    """

    with open(filename, 'r+', encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)  # go back to the beginning of the file to write

        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

        f.truncate()
