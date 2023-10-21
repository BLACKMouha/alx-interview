#!/usr/bin/python3
'''0-nqueens module'''
import sys


def nqueens(n):
    '''NQueens Puzzle Resolver'''
    solutions = []
    board = [[i, None] for i in range(n)]

    cols, posDiag, negDiag = set(), set(), set()

    def helper(row):
        '''Backtrack helper function'''
        if row == n:
            copy = [[row[0], row[1]] for row in board]
            solutions.append(copy)
            return

        for col in range(n):
            if col in cols or (row + col) in posDiag or (row - col) in negDiag:
                continue
            cols.add(col)
            posDiag.add(row + col)
            negDiag.add(row - col)
            board[row][1] = col

            helper(row + 1)

            cols.remove(col)
            posDiag.remove(row + col)
            negDiag.remove(row - col)
            board[row][1] = None

    helper(0)
    return solutions


def printer(lists):
    for li in lists:
        print('{}'.format(li))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            if n < 4:
                print('N must be at least 4')
                exit(1)
            else:
                printer(nqueens(n))
        except ValueError:
            print('N must be a number')
            exit(1)
    else:
        print('Usage: nqueens N')
        exit(1)
