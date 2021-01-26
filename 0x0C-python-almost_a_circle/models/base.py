#!/usr/bin/python3
"""This module creates a class Rectangle"""
import json


class Base:
    """
    This is a Base with:
    - private class attribute __nb_objects
    - class constructor
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes class Base with the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        The static method that returns the JSON string representation
        of list_dictionaries
        - list_dictionaries : is a list of dictionaries
        """
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        The class method that writes the JSON string representation
        of list_objs to a file
        - def to_dictionary(self): returns the dictionary representation of
        Square or Rectangle
        """
        if list_objs is None:
            list_objs = []

        ld = [obj.to_dictionary() for obj in list_objs]

        with open("{}.json".format(cls.__name__), mode="w") as f:
            f.write(cls.to_json_string(ld))

    @staticmethod
    def from_json_string(json_string):
        """
        The static method that returns the list of the JSON string
        representation json_string
        - json_string is a string representing a list of dictionaries
        - If json_string is None or empty, return an empty list
        - Otherwise, return the list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            json_string = []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set:
        - **dictionary can be thought of as a double pointer to a dictionary
        - To assign all attributes: create a Rectangle or Square instance
        with dummy mandatory attributes (width, height, size, etc.)
        - Call update instance method to this dummy instance to apply
        your real values
        - **dictionary must be used as **kwargs of the method update
        """
        if cls.__name__ is "Square":
            dummy = cls(1)
        elif cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy
