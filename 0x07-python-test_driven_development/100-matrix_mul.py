#!/usr/bin/python3
"""
This  module defines a function that multiplies two matrices

The function takes 2 matrices (lists of lists) as input,
validates them according to specific requirements,
and returns their product as a new matrix
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists of int/float): first matrix
        m_b (list of lists of int/float): second one

    Returns:
        TypeError: if m_a or m_b, not a list, not a list of lists,
            if elements are not integers or floats,
            or if rows are not of the same size
        ValueError: if m_a or m_b is empty,
            or if the matrices cannot be multiplied
            due to incompatible dimensions
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    
    for row in m_a:
        if not all(isinstance(ele, (int, float)) for ele in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(ele, (int, float)) for ele in row):
            raise TypeError("m_b should contain only integers or floats")
    
    len_row_a = len(m_a[0])

    if not all(len(row) == len_row_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    len_row_b = len(m_b[0])

    if not all(len(row) == len_row_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    if len_row_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Preform matrix multiplication
    result = [[0 for _ in range(len_row_b)] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len_row_b):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    
    return result
