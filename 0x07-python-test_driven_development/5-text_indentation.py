#!/usr/bin/python3
""" 5-text_indentation module """


def text_indentation(text):
    """ function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    my_list = []
    just_jumped = True

    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if (just_jumped is True and text[i] != ' ') or just_jumped is False:
            print(text[i], end="")
            just_jumped = False
        if text[i] in (".", "?", ":"):
            print()
            print()
            just_jumped = True
