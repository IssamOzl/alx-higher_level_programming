#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

nArgsCount = len(sys.argv) - 1
if nArgsCount != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

sOperator = str(sys.argv[2])
sOperator = sOperator.replace(" ", "")

if sOperator not in ("+", "-", "/", "*"):
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
res = 0

if sOperator == "+":
    res = add(a, b)
elif sOperator == "-":
    res = sub(a, b)
elif sOperator == "*":
    res = mul(a, b)
else:
    res = div(a, b)

print(f"{a} {sOperator} {b} = {res}")
