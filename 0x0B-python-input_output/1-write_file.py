#!/usr/bin/python3
"""This is a module"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8) and
    returns the number of characters written"""

    with open(filename, mode="w+", encoding="utf-8") as f:
        num_chars = f.write(text)
    return num_chars
