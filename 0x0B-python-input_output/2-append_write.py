#!/usr/bin/python3
"""This is a module"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""

    with open(filename, mode="a", encoding="utf-8") as f:
        num_chars = f.write(text)
    return num_chars