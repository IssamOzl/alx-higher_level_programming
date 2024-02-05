#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

    def area(self):
        """ area = l x w """
        return(self.__width * self.__height)

    def __str__(self):
        """ str for print """
        return("[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height))
