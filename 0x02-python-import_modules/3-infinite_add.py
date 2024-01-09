#!/usr/bin/python3

if __name__ != "__main__":
    exit()

from calculator_1 import add
import sys

#-1 to exclude the file name passed as argument
nArgsCount = len(sys.argv) - 1

pCount = 0

for i in range (1, nArgsCount+1):
    pCount = add(pCount, int(sys.argv[i]))
print(pCount)    
