#!/usr/bin/python3
"""
This is the "0-add_integer" module
This module supplies one function - add_integer() - adds 2 integer.
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after each of these characters:'.', '?' and ':'
    """
    if type(text) != str:
        raise TypeError('text must be a string')

    new_text = text.replace('.', '.\n\n')
    new_text = new_text.replace('?', '?\n\n')
    new_text = new_text.replace(':', ':\n\n')

    string = new_text.split('\n')
    for elem in range(len(string)):
        if elem == len(string) - 1:
            print('{}'.format(string[elem].strip()), end="")
        else:
            print('{}'.format(string[elem].strip()), end="\n")
