#!/usr/bin/python3

'''
0-stats script
Reads stdin line by line and computes metrics
'''

import sys

if __name__ == '__main__':
    try:
        sum_file_size = 0
        codes = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
        }
        while True:
            for i in range(10):
                line = input().rstrip().split(' ')
                code = int(line[-2])
                codes[code] += 1
                file_size = line[-1]
                sum_file_size += int(file_size)

            print('File size: {}'.format(sum_file_size))

            for c in codes:
                if (codes[c] != 0):
                    print(f'{c}: {codes[c]}')
            sys.stdin.flush()
    except KeyboardInterrupt as k:
        try:
            for i in range(10):
                line = input().rstrip().split(' ')
                code = int(line[-2])
                codes[code] += 1
                file_size = line[-1]
                sum_file_size += int(file_size)
            print('File size: {}'.format(sum_file_size))
            for c in codes:
                if (codes[c] != 0):
                    print(f'{c}: {codes[c]}')
        except EOFError as eof:
            print(f'File size: {sum_file_size}')
            for c in codes:
                if (codes[c] != 0):
                    print(f'{c}: {codes[c]}')
        finally:
            sys.stdin.flush()
    except ValueError as v:
        print('Status code or File size is not a number :(')
    finally:
        sys.stdin.flush()
