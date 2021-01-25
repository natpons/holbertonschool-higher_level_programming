#!/usr/bin/python3
"""This module creates a class  Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a class Square inherits from Rectangle with:
    - class constructor
    - The overloading __str__ method should return:
    [Square] (<id>) <x>/<y> - <size> - in our case, width or height
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes class Base Square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Returns [Square] (<id>) <x>/<y> - <size> - in our case, width or height
        """
        n = '[Square]'
        a = str(self.id)
        b = str(self.x)
        c = str(self.y)
        d = str(self.size)
        return n + ' (' + a + ') ' + b + '/' + c + ' - ' + d

    @property
    def size(self):
        """
        Getter for size:
        - Uses width attribute from Rectangle parent to store `size`
        - Raises TypeError: if `size` is not an int,
        - ValueError: if `size` is <= 0
        Returns: value associated with `size`
        """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size"""
        self.width = value

    def update(self, *args, **kwargs):
        """
        The public method that assigns the attributs
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if kwargs is not None:
            if 'id' in kwargs.keys():
                self.id = kwargs.get('id')
            if 'size' in kwargs.keys():
                self.size = kwargs.get('size')
            if 'x' in kwargs.keys():
                self.x = kwargs.get('x')
            if 'y' in kwargs.keys():
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """
        The public method that returns the dictionary representation
        of a Rectangle:
        - This dictionary must contain: id, size, x, y
        """
        attrs = ['id', 'size', 'x', 'y']
        return {i: getattr(self, i) for i in attrs}
