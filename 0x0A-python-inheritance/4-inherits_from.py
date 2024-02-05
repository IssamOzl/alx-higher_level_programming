#!/usr/bin/python3
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """ True if obj is a subclass of a_class, otherwise False """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
