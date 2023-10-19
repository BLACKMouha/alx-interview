#!/usr/bin/python3
'''0-rotate_2d_matrix module'''

def rotate_2d_matrix(matrix):
    '''Rotate a 2D matrix'''
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for i in range(n):
        for j in range(int(n / 2)):
            matrix[i] = list(reversed(matrix[i]))