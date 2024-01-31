#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    essorMsg = "{} must be a string"
    if type(first_name) != str:
        raise TypeError(essorMsg.format("first_name"))
    if type(last_name) != str:
        raise TypeError(essorMsg.format("last_name"))
    return print("My name is {} {}".format(first_name, last_name))
