#!/usr/bin/python3
"""This is a module"""


class BaseGeometry:
    """This is an empty class BaseGeometry"""

    def area(self):
        """
        Raises an Exception with the message area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates value
        """
        if type(value) != int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
