#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        rectangle = Rectangle(5, 3)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 3)

    def test_rectangle_area(self):
        rectangle = Rectangle(5, 3)
        self.assertEqual(rectangle.area(), 15)

    def test_rectangle_str(self):
        rectangle = Rectangle(5, 3, 2, 1, 10)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 2/1 - 5/3")

    # Add more test cases for other methods and edge cases


class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_square_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_square_str(self):
        square = Square(5, 2, 1, 10)
        self.assertEqual(str(square), "[Square] (10) 2/1 - 5")

    # Add more test cases for other methods and edge cases


class TestBase(unittest.TestCase):
    def test_base_creation(self):
        base = Base()
        self.assertIsNotNone(base.id)

    def test_base_to_json_string(self):
        base = Base()
        json_string = base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_base_from_json_string(self):
        base = Base()
        list_dictionaries = base.from_json_string('[{"id": 1}, {"id": 2}]')
        self.assertEqual(len(list_dictionaries), 2)

    # Add more test cases for other methods and edge cases


if __name__ == '__main__':
    unittest.main()
