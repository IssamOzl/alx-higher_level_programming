#!/usr/bin/python3

# Variables points to objects EX :
# The 2 vars will point to the same object since str are immutable
a = "banana"
b = "banana"
#print("test")
#print(a == b)
#print(a is b)

# but not in this case because lists are mutable
l1 = [1,2,3]
l2 = [1,2,3]

#Aliasing
l4 = l1

# this is clonning
l3 = l1[:]

print(l1 == l2)
print(l1 is l3)

print("l4 is l1")
print(l4 is l1)
l1[0] = 4
print(l1)
print(l4)
print(l2)

print(l3)

# For loop
# if we want only the value the mos easy is :
fruits = ["banana","apple","orange"]
for fruit in fruits:
    print(fruit)
# for index and value without using for i in range(len(fruits))
for index, val in enumerate(fruits):
    print("{} : {}".format(index, val))
    

