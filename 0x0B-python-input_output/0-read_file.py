#!/usr/bin/python3
""" 0-read_file module """


def read_file(filename=""):
    """ eads a text file (UTF8) and prints it to stdout """
    with open(filename, "r", encoding="UTF-8") as my_file:
        print(my_file.read(), end="")
