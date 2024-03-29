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
        return (self.__size) ** 2

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

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        raise TypeError("unsupported operand type(s) for >:\
         'Square' and '{}'".format(type(other).__name__))

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        raise TypeError("unsupported operand type(s) for >=:\
         'Square' and '{}'".format(type(other).__name__))

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        raise TypeError("unsupported operand type(s) for <:\
         'Square' and '{}'".format(type(other).__name__))

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        raise TypeError("unsupported operand type(s) for <=:\
         'Square' and '{}'".format(type(other).__name__))
