#!/usr/bin/python3
"""
This is the "Rectangle"  module.

This module provides a simple Rectangle class.
"""


class Rectangle:
    """A simple Rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")

        self.__width = val

    @property
    def height(self):
        self.__height = height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val
