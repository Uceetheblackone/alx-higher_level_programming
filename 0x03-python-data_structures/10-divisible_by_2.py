#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ finds all multiples of 2 in a list."""
    multiples = []
    for item in range(len(my_list)):
        if my_list[item] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
