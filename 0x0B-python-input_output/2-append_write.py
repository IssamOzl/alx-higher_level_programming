#!/usr/bin/python3
""" 2-append_write """


def append_write(filename="", text=""):
    """  appends a string at the end of a text file """
    nb_chars = 0
    with open(filename, "a", encoding="UTF-8") as my_file:
        nb_chars = my_file.write(text)
    return nb_chars
