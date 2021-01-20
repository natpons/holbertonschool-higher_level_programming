#!/usr/bin/python3
"""This is a module"""

import json


def from_json_string(my_str):
    """A function that returns the object (Python data structure)
    represented by a JSON string"""

    return json.loads(my_str)
