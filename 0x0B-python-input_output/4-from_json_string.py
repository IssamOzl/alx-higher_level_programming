#!/usr/bin/python3
""" 4-from_json_string """
import json


def from_json_string(my_str):
    """ eturns the JSON representation of an object (string) """
    return json.loads(my_str)
