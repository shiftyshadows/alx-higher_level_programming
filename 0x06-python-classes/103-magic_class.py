#!/usr/bin/python3
""" Defines a class MagicClass """
import math

class MagicClass:
    """ This represents a circle """
    def __init__(self, radius=0):
        """ Initializes the Magic Class
            Args:
                Radius
        """
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
