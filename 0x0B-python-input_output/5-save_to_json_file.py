#!/usr/bin/python3
""" 5-save_to_json_file module """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON represent """
    with open(filename, "w", encoding="UTF-8") as my_file:
        my_file.write(json.dumps(my_obj))
