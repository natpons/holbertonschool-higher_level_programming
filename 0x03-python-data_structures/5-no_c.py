#!/usr/bin/python3
def no_c(my_string):
    string = []
    for char in my_string:
        my_string.translate({ord('c'): None, ord('C'): None})
        string = my_string.translate({ord('c'): None, ord('C'): None})

    return string
