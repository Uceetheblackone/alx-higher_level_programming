#!/usr/bin/python3
def uppercase(s):
    for c in s:
        print("")
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
