#!/usr/bin/python3

def print_list_integer(my_list=[]):
    nCount = len(my_list)
    for i in range(0, nCount):
        print(f"{my_list[i]}")

a = [10,2,3]
print_list_integer(a)


