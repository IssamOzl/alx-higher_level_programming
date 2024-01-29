#!/usr/bin/python3

def print_square(size):
    my_char = "#"
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print(my_char,end="")
        print()
