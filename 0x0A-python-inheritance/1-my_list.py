#!/usr/bin/python3
"""
This is a module for class MyList that inherits from list:
- public instance method print_sorted() that prints list
"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """Prints the sorted list (ascending sort)"""
        print(sorted(self))
