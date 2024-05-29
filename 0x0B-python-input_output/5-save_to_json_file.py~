#!/usr/bin/python3
""" 5-save_to_json_file module """
to_json_string = __import__('3-to_json_string').to_json_string


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON represent """
    s_myobj = to_json_string(my_obj)
    with open(filename, "w", encoding="UTF-8") as my_file:
        my_file.write(s_myobj)
