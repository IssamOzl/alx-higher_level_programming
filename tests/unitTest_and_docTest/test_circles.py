#!/usr/bin/python3

from math import pi
from circles import circle_area
import unittest

class TestCircleArea(unittest.TestCase):
    def tpVerif(self):
        # test that int is passed as param
        self.assertRaises(TypeError,circle_area,'me')
        self.assertRaises(TypeError,circle_area,True)
        self.assertRaises(TypeError,circle_area,3+5j)
