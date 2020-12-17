#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    for key, value_current in new.items():
        if value_current == value:
            del a_dictionary[key]

    return a_dictionary
