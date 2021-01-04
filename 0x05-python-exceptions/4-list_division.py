#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    j = 0
    for i in range(list_length):
        value = 0
        try:
            value = my_list_1[i] / my_list_2[i]
        except ValueError:
            value = 0
        except TypeError:
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        finally:
            new_list[j] = value
            j = j + 1
    return new_list
