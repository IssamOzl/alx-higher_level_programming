#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    newDic = a_dictionary.copy()
    for i, v in newDic.items():
        newDic[i] = v * 2
    return newDic
