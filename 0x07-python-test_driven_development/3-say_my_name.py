#!/usr/bin/python3
"""
This is the "3-say_my_name" module
This module supplies one function - say_my_name
- that prints first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
