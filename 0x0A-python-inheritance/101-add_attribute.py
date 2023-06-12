#!/usr/bin/python3
"""
This module contains the add_attribute function
"""


def add_attribute(obj, attribute, value):
    """function that adds a new attribute to an object if it’s possible"""
    if hasattr(obj, attribute):
        """If the object has the attribute, raise a TypeError with appropriate message"""
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
