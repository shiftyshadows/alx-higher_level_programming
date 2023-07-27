#!/usr/bin/python3
"""
This is a mattrix multiplication module
It supplies one function that multiplies 2 matices
"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices. """
    if type(m_a) is not list or type(m_b) is not list:
        raise TypeError("Matrix must be a list")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("Matrix can't be empty")

    for item in m_a:
        if type(item) is not list:
            raise TypeError("Matrix must be a list of lists")
        if len(item) == 0:
            raise ValueError("Matrix can't be empty")
        for element in item:
            if type(element) not in (int, float):
                raise TypeError("Matrix should contain only integers/floats")
    row_sizes = {len(item) for item in m_a}
    if len(row_sizes) > 1:
        raise ValueError("Each row of the matrix must be of the same size")

    for item in m_b:
        if type(item) is not list:
            raise TypeError("Matrix must be a list of lists")
        if len(item) == 0:
            raise ValueError("Matrix can't be empty")
        for element in item:
            if type(element) not in (int, float):
                raise TypeError("Matrix should contain only integers/floats")
    row_sizes = {len(item) for item in m_b}
    if len(row_sizes) > 1:
        raise ValueError("Each row of the matrix must be of the same size")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem = 0
            for k in range(len(m_a[i])):
                elem += m_a[i][k] * m_b[k][j]
            row.append(elem)
        result.append(row)

    return result
