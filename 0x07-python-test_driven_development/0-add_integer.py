#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """ Returns the result of addition of 2 integers"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return int(a + b)
