#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    order_list = sorted(a_dictionary.keys())
    for key in order_list:
        value = a_dictionary[key]
        print(key,value)
