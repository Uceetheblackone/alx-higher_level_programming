#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """ 
    # function that prints an integer.
    # with value as any type.
    # Safe_print_integer(int): prints with error message.
    # Returns: true if value is printed correctly otherwise false.
    """

    try:

        print("{:d}".format(value))

    except (TypeError, ValueError) as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return (False)

    return (True)
