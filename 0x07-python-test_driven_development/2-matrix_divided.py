#!/usr/bin/python3

def matrix_divided(matrix, div):
    mtTypeError = "matrix must be a matrix (list of lists) of integers/floats"
    
    if type(div) not in(int,float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError(mtTypeError)
    
    
    for i in range(len(matrix)):
        if type(matrix[i]) != list or len(matrix[i]) == 0:
            raise TypeError(mtTypeError)
        if i == 0:
            initSize = len(matrix[0])
        if len(matrix[i]) != initSize:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in (int,float):
                raise TypeError(mtTypeError)
            matrix[i][j] = round(matrix[i][j] / div,2)

    return matrix