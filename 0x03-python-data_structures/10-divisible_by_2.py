#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ finds all multiples of 2 in a list."""
    mult = []
    for item in my_list:
        if item % 2 == 0:
            mult.append(True)
        else:
            mult.append(False)
    return mult

