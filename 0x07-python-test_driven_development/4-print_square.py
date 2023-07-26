#!/usr/bin/python3
"""
This is 4-print_square module.
The module defines a single function, print_square
"""


def print_square(size):
    """ Function that prints a square with the character #."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
