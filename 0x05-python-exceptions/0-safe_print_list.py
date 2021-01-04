#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for items in range(x):
            print("{}".format(my_list[items]), end="")
    except IndexError:
        return items
    else:
        return x
    finally:
        print("")
