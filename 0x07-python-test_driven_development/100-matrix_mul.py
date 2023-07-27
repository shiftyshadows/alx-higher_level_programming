#!/usr/bin/python3
"""
This is a mattrix multiplication module
It supplies one function that multiplies 2 matices
"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices. """
    if type(m_a) is not list or type(m_b) is not list:
        if type(m_a) is not list:
            raise TypeError("m_a must be a list")
        if type(m_b) is not list:
            raise TypeError("m_b must be a list")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("Matrix can't be empty")

    for item in m_a:
        if type(item) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(item) == 0:
            raise ValueError("m_a can't be empty")
        for element in item:
            if type(element) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    row_sizes = {len(item) for item in m_a}
    if len(row_sizes) > 1:
        raise ValueError("each row of m_a must be of the same size")

    for item in m_b:
        if type(item) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(item) == 0:
            raise ValueError("m_b can't be empty")
        for element in item:
            if type(element) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
    row_sizes = {len(item) for item in m_b}
    if len(row_sizes) > 1:
        raise ValueError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")


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
