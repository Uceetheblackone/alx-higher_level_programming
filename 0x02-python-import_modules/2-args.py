#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number and list of arguments."""
    import sys

    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 arguments.")
    else:
        print("{} arguments.".format(num_args))
        for a in range(num_args):
            print("{}: {}".format(a + 1, args[a]))

