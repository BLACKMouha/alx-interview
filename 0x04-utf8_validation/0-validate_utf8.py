#!/usr/bin/python3
'''0-validate_utf8 script'''


def validUTF8(data):
    '''determines if a given data set represents a valid UTF-8 encoding
    Arg:
        data: a list of integers, each one corresponding to a character
    Return:
        True when all the characters are ASCII else False.'''
    try:
        return bytearray(data).isascii()
    except Exception as e:
        return False
