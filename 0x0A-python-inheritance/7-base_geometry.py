#!/usr/bin/python3
""" 6-base_geometry """


class BaseGeometry:
    """ Geometry Class """
    def area(self):
        """ Not Yet Implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator method """
        myErrors = [
            "{} must be an integer",
            "{} must be greater than 0"
        ]
        if type(value) is not int:
            raise TypeError(myErrors[0].format(name))
        if value <= 0:
            raise ValueError(myErrors[0].format(name))
