#!/usr/bin/python3
"""
This is the "0-add_integer" module

This module supplies one function - add_integer() - adds 2 integer.
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers and return the result
    """
    inf = float('inf')
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if a == inf:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    if b == inf:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
