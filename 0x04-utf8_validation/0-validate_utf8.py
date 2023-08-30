#!/usr/bin/python3
'''0-validate_utf8 script'''


def validUTF8(data):
    '''determines if a given data set represents a valid UTF-8 encoding
    Arg:
        data: a list of integers, each one corresponding to a character
    Return:
        True when the data set follows the UTF8 rules otherwise False'''
    n_bytes = 0
    for num in data:
        bits = bin(num).lstrip('0b').zfill(8)
        if n_bytes == 0:
            for bit in bits:
                if bit == '0':
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (bits[0] == '1' and bits[1] == '0'):
                return False
        n_bytes -= 1
    return n_bytes == 0
