#!/usr/bin/python3

import sys

if __name__ != "__main__":
    exit()

title = " argument"
countArgs = len(sys.argv) - 1
title = str(countArgs) + title

if countArgs == 0:
    title += "s."
elif countArgs == 1:
    title += ":"
else:
    title += "s:"

print(title)
for i in range(1, countArgs+1):
    print(f"{i} : {sys.argv[i]}")
