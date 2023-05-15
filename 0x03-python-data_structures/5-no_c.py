#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string."""
    new_string = []
    for m in my_string:
        if m != 'c' and m != 'C':
            new_string.append(m)
    return ''.join(new_string)

