#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nRes = []

    for insideList in matrix:
        nMyl = []
        for val in insideList:
            nMyl.append(val**2)
        nRes.append(nMyl)
    return nRes


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(square_matrix_simple(matrix))
