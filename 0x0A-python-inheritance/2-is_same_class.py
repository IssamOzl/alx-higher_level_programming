#!/usr/bin/python3
""" 2-is_same_class module """


def is_same_class(obj, a_class):
    """ check if the object is exactly an instance of a class"""
    return (type(obj) is a_class)
