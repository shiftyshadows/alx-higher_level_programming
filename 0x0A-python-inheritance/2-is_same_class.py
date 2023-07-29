#!/usr/bin/python3
"""
This module returns True if the object is exactly an instance of
the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """This defines the stated function"""
    return type(obj) is a_class
