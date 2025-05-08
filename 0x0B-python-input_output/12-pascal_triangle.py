#!/usr/bin/python3
"""
This module defines a function that returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of int representing the Pascal's triangle of n

    Args:
        n (int): the number of rows in the triangle

    Returns:
        list: a list of lists representing the triangle
        []: if n <= 0
    """

    if n <= 0:
        return []

    triangle = [[1]]  # initialize the triangle with first row

    for i in range(1, n):
        row = [1]  # the first element of each row is always 1
        prev_row = triangle[i - 1]  # get the previous row

        for j in range(1, i):
            # Calculate the elements based on the sum of the two elements above
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # the last element of each row is always 1
        triangle.append(row)  # add the row to the triangle

    return triangle
