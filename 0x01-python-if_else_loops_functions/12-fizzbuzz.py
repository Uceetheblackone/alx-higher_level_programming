#!/usr/bin/python3
def fizzbuzz():
    """Print numbers from 1 to 100 separated by a space in between them.
    for multiples of three, print Fizz.
    for multiples of five, print Buzz.
    for multiples of three and five, print FizzBuzz.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end= "")
