#!/usr/bin/python3
"""This is a module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Instantiation with width and height
        width and height must be private. No getter or setter
        width and height must be positive integers,
        validated by integer_validator
        """
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

    def area(self):
        """
        Public instance method that calculate rectangles area
        """
        return self.__width * self.__height

    def __str__(self):
        """ Return the rectangle description: [Rectangle] <width>/<height>"""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
