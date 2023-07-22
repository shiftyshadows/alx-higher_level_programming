#!/usr/bin/python3
""" Defines a class with name square """


class Square:
    """ Square class attributes
        Attributes:
            __size(int): size of side of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a Square
            Args:
                size(int): size of side of square
                position (tuple): the coordinates of the square.
            Return: None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) == tuple and len(value) == 2 and \
            type(value[0]) == int and type(value[1]) == int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """ Prints the square with the # character on stdout."""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
