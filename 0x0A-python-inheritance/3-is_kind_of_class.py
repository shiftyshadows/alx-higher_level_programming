#!/usr/bin/pytthon3
"""This module defines a function that returns True or False"""


def is_kind_of_class(obj, a_class):
    """
       This method returns True if the object is an instance of,
       or if the object is an instance of a class that inherited from,
       the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
