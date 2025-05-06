#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from int and inverts ==
and != operators.
"""


class MyInt(int):
    """
    A rebel class that inherits from int and inverts == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the behavior of the == operator

        Args:
            other: the value to compare with

        Returns:
            bool: True if the values are not equal, False otherwise
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the != operator

        Args:
        other: the value to compare with

        Returns:
        bool: True if the values are not equal, False otherwise
        """
        return super().__eq__(other)
