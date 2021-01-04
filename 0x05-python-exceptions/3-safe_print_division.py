#!/usr/bin/python3
def safe_print_division(a, b):
    value = None
    try:
        value = a / b
        return value
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result:", "{}".format(value))
