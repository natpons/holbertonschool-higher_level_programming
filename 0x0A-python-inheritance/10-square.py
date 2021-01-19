#!/usr/bin/python3
"""This is a module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    def __init__(self, size):
        """
        Instantiation with size
        size must be private. No getter or setter
        size must be a positive integer,
        validated by integer_validator
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Public instance method that calculate Square area
        """
        return self.__size ** 2
