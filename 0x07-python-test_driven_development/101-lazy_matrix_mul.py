#!/usr/bin/python3
"""
This  module defines a function that multiplies two matrices
using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using Numpy.

    Args:
        m_a (list of lists of int/float): first matrix
        m_b (list of lists of int/float): second one

    Returns:
        list of lists: the result of the multiplication

    Raises:
        TypeError: if m_a or m_b, not a list
        TypeError: if elements of m_a or m_b are not int/floats
        TypeError: if m_a or m_b are not of the same size
        ValueError: if m_a or m_b is empty,
        ValueError: if m_a and m_b can't be multiplied
    """
    # Input validation using NumPy, which will raise exceptions
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    for row in m_a:
        if not all(isinstance(ele, (int, float)) for ele in row):
            raise TypeError("invalid data type for einsum")
    for row in m_b:
        if not all(isinstance(ele, (int, float)) for ele in row):
            raise TypeError("invalid data type for einsum")

    # Check for consistent row sizes before converting to NumPy arrays
    len_row_a = [len(row) for row in m_a]
    if not all(size == len_row_a[0] for size in len_row_a):
        raise TypeError("setting an array element with a sequence.")

    len_row_b = [len(row) for row in m_b]
    if not all(size == len_row_b[0] for size in len_row_b):
        raise TypeError("setting an array element with a sequence.")

    try:
        # Convert to NumPy arrays
        np_a = np.array(m_a)
        np_b = np.array(m_b)

        # Perform matrix multiplication
        # using NumPy's matmul function
        result = np.matmul(np_a, np_b)

        return result

    except ValueError:
        if any(len(row) != len(m_a[0]) for row in m_a[1:]):
            raise TypeError(
                "setting an array element with a sequence."
                ) from None
        if any(len(row) != len(m_b[0]) for row in m_b[1:]):
            raise TypeError(
                "setting an array element with a sequence."
                ) from None
        raise  # Re-raise if it's note the "sequence" error

    except ValueError as e:
        err = "shapes {} and {} not aligned: {} (dim 1) != {} (dim 0)"
        raise ValueError(
            err.format(
                np_a.shape, np_b.shape, np_a.shape[1], np_b.shape[0]
                )
            ) from None
    except TypeError as e:
        raise TypeError("invalid data type for einsum") from None
