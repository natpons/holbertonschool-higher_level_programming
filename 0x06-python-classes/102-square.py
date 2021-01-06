#!/usr/bin/python3
"""This module creates a class Square"""


class Square:
    """
    This is a class Square that defines a square
    by a private instance attribute: size
    - property def size(self): to retrieve size
    - property setter def size(self, value): to set size
    - size must be a number(float or integer)
    - raise error exceptions on invalid inputs
    - instantiation with size: def __init__(self, size=0)
    - public instance method: def area(self): returns the square area size
    - square instance can answer to comparators:
    ==, !=, >, >=, < and <= (compares square area between Square objects)
    """

    def __init__(self, size=0):
        """
        Initializes class Square with optional size
        """
        self.size = size

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

    @size.setter
    def size(self, value):
        """ to set value - defines value of class Square size """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def __eq__(self, other):
        """ Square instance answer to comparator: == """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Square instance answer to comparator: != """
        return self.area() != other.area()

    def __gt__(self, other):
        """ Square instance answer to comparator: > """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Square instance answer to comparator: >= """
        return self.area() >= other.area()

    def __lt__(self, other):
        """ Square instance answer to comparator: < """
        return self.area() < other.area()

    def __le__(self, other):
        """ Square instance answer to comparator: <= """
        return self.area() <= other.area()
