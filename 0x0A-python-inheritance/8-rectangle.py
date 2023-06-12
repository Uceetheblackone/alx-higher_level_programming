#!/usr/bin/python3

"""
This module contains class basegeometry and subclass rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """A class Rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
