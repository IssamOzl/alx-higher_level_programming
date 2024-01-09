#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    nCount = len(my_list)
    if nCount >= idx or idx < 0:
        return my_list

    new_list = my_list
    new_list[idx] = element
    return (new_list)
