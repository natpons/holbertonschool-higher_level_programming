#!/usr/bin/python3
"""
This is the "0-add_integer" module
This module supplies one function - add_integer() - adds 2 integer.
"""


def print_square(size):
    """ Prints a square with the character # """
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
