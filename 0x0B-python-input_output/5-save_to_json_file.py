#!/usr/bin/python3
"""This is a module"""

import json


def save_to_json_file(my_obj, filename):
    """A function that writes the Object to a text file,
    using JSON representation"""

    with open(filename, mode="w") as f:
        return json.dump(my_obj, f)
