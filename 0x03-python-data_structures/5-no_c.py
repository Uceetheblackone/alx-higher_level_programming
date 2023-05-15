#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for m in my_string:
        if m != 'c' and m != 'C':
            new_string.append(m)
    return ''.join(new_string)

