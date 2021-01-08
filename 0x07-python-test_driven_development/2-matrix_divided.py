#!/usr/bin/python3
"""
This is the "2-matrix_divided" module
This module supplies one function - matrix_divided()
- divides all elementss of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    list_err = 'matrix must be a matrix (list of lists) of integers/floats'

    if type(matrix) != list:
        raise TypeError(list_err)

    if matrix == [[]] or matrix == [] or matrix == [[], []]:
        raise TypeError(list_err)

    for row in matrix:
        if type(row) != list:
            raise TypeError(list_err)
        for elem in row:
            if isinstance(elem, (int, float)) is False:
                raise TypeError(list_err)
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        if isinstance(div, (int, float)) is False:
            raise TypeError('div must be a number')
        else:
            new_matrix.append([round((elements / div), 2) for elements in row])

    return new_matrix
