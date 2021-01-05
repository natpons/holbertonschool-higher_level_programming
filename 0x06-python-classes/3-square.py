#!/usr/bin/python3
"""This module creates a class Square"""


class Square:
    """
    This is a class Square that defines a square
    by a private instance attribute: size
    """

    def __init__(self, size=0):
        """
        Initializes class Square with optional size
        """
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """
        Public instance method that returns the current square area
        """
        return self.__size * self.__size
