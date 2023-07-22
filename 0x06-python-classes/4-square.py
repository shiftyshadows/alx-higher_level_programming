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
        self.size = size

    def area(self):
        """ Calculates the square's area
            Returns: The area of the square
        """

    @property
    def size(self):
        """ Getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter of __size
        Args: value (int): the size of a size of the square
        Returns: None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
