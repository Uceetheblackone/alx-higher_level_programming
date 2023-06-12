#!/usr/bin/python3

"""
This module contains class basegeometry
"""


class BaseGeometry:
    """A class with public instance method area and integer_validator"""
    def area(self):
        """function that raises an exception with an area message when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
