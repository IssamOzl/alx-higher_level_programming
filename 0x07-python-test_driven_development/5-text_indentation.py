#!/usr/bin/python3

def text_indentation(text):
    my_list = []
    just_jumped = True
    
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if (just_jumped == True and text[i] != ' ') or just_jumped == False:
            print(text[i],end="")
            just_jumped = False
        if text[i] in (".","?",":"):
            print()
            print()
            just_jumped = True
