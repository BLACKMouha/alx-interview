#!/usr/bin/pyhon3
"""
0-main
"""

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle


def print_triangle(triangle):
    """
    Prints a pascal triangle
    Arg:
        triangle: a 2D list of numbers
    Return: Nothing
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == '__main__':
    print_triangle(pascal_triangle(5))
