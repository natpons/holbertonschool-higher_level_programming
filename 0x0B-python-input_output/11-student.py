#!/usr/bin/python3
"""This module creates a class Student"""


class Student:
    """
    This is a class Student that defines a student by
    Public instance attributes: first_name, last_name, age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes of class Student with first_name, last_name, age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation
        of a Student instance"""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        """Public method def reload_from_json(self, json):
        that replaces all attributes of the Student instance:
        - json will always be a dictionary
        - a dictionary key will be the public attribute name
        - a dictionary value will be the value of the public attribute"""
        for items in json:
            self.__dict__[items] = json[items]
