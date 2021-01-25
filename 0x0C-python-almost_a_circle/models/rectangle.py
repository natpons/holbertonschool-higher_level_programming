#!/usr/bin/python3
"""This module creates a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    This is a class Rectangle inherits from Base with:
    - private instance attributes
    - class constructor
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes class Base with the private instance attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """to retrieve width, returns value"""
        return self.__width

    @width.setter
    def width(self, value):
        """ to set width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        to retrieve height, returns value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ to set width"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """to retrieve x, returns value"""
        return self.__x

    @x.setter
    def x(self, value):
        """ to set x"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """to retrieve y, returns value"""
        return self.__y

    @y.setter
    def y(self, value):
        """ to set x"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Public method that returns the area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        Public method that prints in stdout the Rectangle instance
        with the character #
        - by taking care of x and y
        """
#        for i in range(self.__height):
#           for j in range(self.__width):
#               print('#', end="")
#           print()

        if self.__height == 0 or self.__width == 0:
            print()
        else:
            for i in range(self.__y):
                print()
            for i in range(self.__height):
                for j in range(self.__x):
                    print(' ', end="")
                for j in range(self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        """ Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        n = '[Rectangle]'
        a = str(self.id)
        b = str(self.__x)
        c = str(self.__y)
        d = str(self.__width)
        e = str(self.__height)
        return n + ' (' + a + ') ' + b + '/' + c + ' - ' + d + '/' + e

    def update(self, *args, **kwargs):
        """
        The public method that:
        - assigns an argument to each attribute with args (ex8)
        - assigns a key/value argument to attributes (ex9)
        - **kwargs must be skipped if *args exists and is not empty (ex9)
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

        if kwargs is not None:
            if 'id' in kwargs.keys():
                self.id = kwargs.get('id')
            if 'width' in kwargs.keys():
                self.__width = kwargs.get('width')
            if 'height' in kwargs.keys():
                self.__height = kwargs.get('height')
            if 'x' in kwargs.keys():
                self.__x = kwargs.get('x')
            if 'y' in kwargs.keys():
                self.__y = kwargs.get('y')

    def to_dictionary(self):
        """
        The public method that returns the dictionary representation of a Rectangle:
        - This dictionary must contain: id, width, height, x, y
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        return {i: getattr(self, i) for i in attrs}
