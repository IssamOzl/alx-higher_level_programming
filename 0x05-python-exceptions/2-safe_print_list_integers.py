#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    nbprint = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end = "")
            nbprint += 1
        except Exception:
            continue
    print()
    return nbprint

lst = [1,2,3]
safe_print_list_integers(lst,2)
