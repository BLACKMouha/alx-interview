#!/usr/bin/python3
"""0-minoperations module"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly
    n 'H' characters in a file.
    """
    num_ops = 0
    min_num_ops = 2
    while n > 1:
        while n % min_num_ops == 0:
            num_ops += min_num_ops
            n /= min_num_ops
        min_num_ops += 1
    return num_ops
