#!/usr/bin/python3
''' pascal_triangle module '''

'''
For a row x, the number of elements is x + 1
For a row x, elements at at column 0 and x are set to 1
All other elements are got with the sum of the two numbers just above it.
This means for a row x, an integer at column y is got by the sum of element at
[x-1, y-1] + [x-1, y]
At row 0, we have a list of 1 element composed by 1
At row 1, we have a list of 2 elements composed by 1, 1
And so on.
So for a row x, the number of elements is x + 1

x is between 0 and n (n excluded)
y is between 0 and x (x included)

A sublist is a sequence of numbers got witht the sum of two elements above it.
Each sublist is appended to main list, and in turn the main is returned by the
function.
'''

def pascal_triangle(n):
    '''
    Build a Pascal Triangle of leng @n

    Args:
        n: integer, the number of rows in the Triangle
    Return: return a list of list of numbers like a triangular array of numbers
    '''
    t, s = [], []

    for i in range(n):
        s = []
        for j in range(i + 1):
            if j == 0 or j == i:
                s.append(1)
            else:
                s.append(t[i-1][j-1] + t[i-1][j])
        t.append(s)
    return t
