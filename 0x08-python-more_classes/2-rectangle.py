#!/usr/bin/python3
"""This module creates a class Rectangle"""


class Rectangle:
    """
    This is a class Rectangle that defines a rectangle
    by the private instance attributes width and height
    """

    def __init__(self, width=0, height=0):
        """
        Initializes class Rectangle with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        to retrieve width - defines width of class Rectangle, returns value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ to set width - defines value of class Rectangle width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        to retrieve height - defines height of class Rectangle, returns value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ to set height - defines value of class Rectangle height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Public instance method that returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method that returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*(self.__width + self.__height)
