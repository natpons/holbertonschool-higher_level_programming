#!/usr/bin/python3
"""This module creates a class Rectangle"""


class Rectangle:
    """
    This is a class Rectangle that defines a rectangle
    by the private instance attributes width and height
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes class Rectangle with optional width and height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """ Return the rectangle as # string """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            for row in range(self.__height):
                string = string + (str(self.print_symbol) * self.__width)
                if row != len(range(self.__height)) - 1:
                    string = string + '\n'
            return string

    def __repr__(self):
        """
        Return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
        Delete an instance of Rectangle
        """
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area
        """

        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() <= rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Class method returns a new Rectangle instance with w == h == size
        """
        return Rectangle(size, size)
