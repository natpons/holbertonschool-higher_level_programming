#!/usr/bin/python3
"""This module creates a class Square"""


class Square:
    """
    This is a class Square that defines a square
    by a private instance attribute: size
    """

    def __init__(self, size):
        """
        Initializes class Square by size
        """
        self.__size = size
