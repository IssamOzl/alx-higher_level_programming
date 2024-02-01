#!/usr/bin/python3
def magic_string(string=[]):
    print(id(string))
    string.append("BestSchool")
    return ", ".join(string)
