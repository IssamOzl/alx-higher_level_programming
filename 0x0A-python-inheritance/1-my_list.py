#!/usr/bin/python3
""" 1-my_lis module """


class MyList(list):
    """Class with method print_sorted"""
    
    def print_sorted(self):
        """ Return sorted list """
        print(sorted(list(self)))
