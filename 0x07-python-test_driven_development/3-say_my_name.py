#!/usr/bin/python3
"""
This  module defines a function that prints a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.
            Defaults to ""

    Raises:
        TypeError: If first_name/last_name is not str.
    """

    if not isinstance(first_name, str):
        raise TypeError(
            "first_name must be a string"
        )

    if not isinstance(last_name, str):
        raise TypeError(
            "last_name must be a string"
        )

    print(f"My name is {first_name} {last_name}")
