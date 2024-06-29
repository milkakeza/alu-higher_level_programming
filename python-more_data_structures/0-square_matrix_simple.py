#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    newmatr = []
    for i in matrix:
        res = list(map(lambda x: x**2, i))
        newmatr.append(res)
    return newmatr
