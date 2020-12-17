#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, value_current in a_dictionary.items():
        if value_current == value:
            del a_dictionary[key]

    return a_dictionary
