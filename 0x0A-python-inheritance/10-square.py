#!/usr/bin/python3
""" This module contains the classes Rectangle & Square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class with public instance methods"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)

    def __str__(self):
        return f"[Square] {self._Rectangle__width}"

    def __repr__(self):
        return f"Square({self._Rectangle__width})"
