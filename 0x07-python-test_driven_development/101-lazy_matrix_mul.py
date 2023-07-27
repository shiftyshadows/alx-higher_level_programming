#!/usr/bin/python3
"""
This is lazy matrix multiplication module
The module defines a function that multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This function multiplies two matrices using numpy"""
    return (np.matmul(m_a, m_b))
