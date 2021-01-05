#!/usr/bin/python3
"""This module creates a class Square"""


class Square:
    """
    This is a class Square that defines a square
    by a private instance attribute: size
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes class Square with optional size and position
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Public instance method that returns the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        to retrieve size - defines size of class Square, returns value of size
        """
        return self.__size

    @property
    def position(self):
        """
        to retrieve size - defines position and return value of it
        """
        return self.__position

    @size.setter
    def size(self, value):
        """ to set value - defines value of class Square size """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @position.setter
    def position(self, value):
        """ to set position - defines value of class Square position """
        for item in value:
            if not isinstance(item, int) and item > 0 and len(value) != 2:
                raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
