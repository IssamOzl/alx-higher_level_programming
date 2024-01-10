#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nRes = []

    for insideList in matrix:
        nMyl = []
        for val in insideList:
            nMyl.append(val**2)
        nRes.append(nMyl)
    return nRes
