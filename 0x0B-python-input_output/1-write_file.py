#!/usr/bin/python3
""" 1-write_file module """


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)"""
    nb_ligne = 0
    with open(filename, "w", encoding="UTF-8") as my_file:
        nb_ligne = my_file.write(text)
    return nb_ligne
