#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = []
    if search not in my_list:
        newList = myList
    else:
        newList = [x if x != search else replace for x in my_list]

    return newList
