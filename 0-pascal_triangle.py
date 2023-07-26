#!/usr/bin/python3
''' pascal_triangle module '''


from math import factorial


def binomial_coef(x, y):
    '''
    Computes binomial coefficient of two integers

    Args:
        x: integer, must be greater than or equal to y
        y: integer, must be less than or equal to x
    Return: an integer, the binomial coefficient on success.
            On failure, -1 is returned
    '''
    if x < 0 or y < 0 or x < y:
        return -1
    return int(factorial(x) / (factorial(y) * factorial(x - y)))


def pascal_triangle(n):
    '''
    Builds a Pascal's Triangle of lenght @n:

    Args:
        n: an integer representing the number of rows in the triangle
    Return: a list of list of integers like a triangular array of numbers.
    '''

    if n <= 0:
        return []

    t, s = [], []
    b = 0

    for i in range(n):
        s = []
        for j in range(i + 1):
            b = binomial_coef(i, j)
            s.append(b)
        t.append(s)
    return t
