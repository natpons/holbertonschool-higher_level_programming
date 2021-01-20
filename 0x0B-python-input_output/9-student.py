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

    def to_json(self):
        """Public method that retrieves a dictionary representation
        of a Student instance"""
        return self.__dict__
