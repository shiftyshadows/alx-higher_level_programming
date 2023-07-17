#!/usr/bin/python3
import json
import turtle
import csv

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    instance = cls.create_from_csv_row(row)
                    instances.append(instance)
        except FileNotFoundError:
            pass
        return instances

    def to_csv_row(self):
        raise NotImplementedError("Subclasses must implement the to_csv_row method.")

    @classmethod
    def create_from_csv_row(cls, row):
        raise NotImplementedError("Subclasses must implement the create_from_csv_row method.")

    @staticmethod
    def draw(list_rectangles, list_squares):
        window = turtle.Screen()
        turtle.speed(0)  # Set the turtle speed to the fastest
        turtle.penup()  # Lift the pen up to avoid drawing while moving
        for rectangle in list_rectangles:
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()  # Put the pen down to start drawing
            turtle.color("blue")  # Set the color of the rectangle
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.right(90)
                turtle.forward(rectangle.height)
                turtle.right(90)
            turtle.penup()  # Lift the pen up after drawing the rectangle
        for square in list_squares:
            turtle.goto(square.x, square.y)
            turtle.pendown()  # Put the pen down to start drawing
            turtle.color("red")  # Set the color of the square
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.penup()  # Lift the pen up after drawing the square
        turtle.done()
