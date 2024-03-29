#!/usr/bin/python3
""" Defines a class with name square """


class Square:
    """ Square class attributes
        Attributes:
            __size(int): size of side of square
    """
    def __init__(self, size=0):
        """ Initializes a Square
            Args:
                size(int): size of side of square
            Return: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """ Calculates the square's area
            Returns: The area of the square
        """
        return self.__size ** 2
