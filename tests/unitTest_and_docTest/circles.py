#!/usr/bin/python3
from math import pi

def circle_area(r):
    """
    >>> from math import pi
    >>> res = pi
    >>> res == circle_area(1)
    True
 """
    if type(r) not in (int,float):
        raise TypeError("type of r must be int or float")
    if r < 0:
        raise ValueError("r must be >0")
    return pi*(r**2)
