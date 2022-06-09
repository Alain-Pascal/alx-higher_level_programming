#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = [[r ** 2 for r in row] for row in matrix]
    return (matrix_new)
