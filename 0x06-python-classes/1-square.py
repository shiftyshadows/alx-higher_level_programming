#!/usr/bin/python3
""" Defines a class with name square """


class Square:
    """ Square class attributes
        Attributes:
            __size(int): size of side of square
    """
    def __init__(self, size):
        """ Initializes a Square
            Args:
                size(int): size of side of square
            Return: None
        """
        self.__size = size
