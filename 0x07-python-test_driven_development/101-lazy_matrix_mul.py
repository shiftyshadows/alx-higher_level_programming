#!/usr/bin/python3
"""
This is lazy matrix multiplication module
The module defines a function that multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This function multiplies two matrices using numpy"""
    # Convert input matrices to NumPy arrays
    np_m_a = np.array(m_a)
    np_m_b = np.array(m_b)

    # Perform matrix multiplication using NumPy
    result = np.dot(np_m_a, np_m_b)

    return result.tolist()
