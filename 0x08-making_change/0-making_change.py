#!/usr/bin/python3
'''0-making_change module'''


def makeChange(coins: list, total: int):
    '''Making change'''
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    numCoins = 0

    for coin in coins:
        while total >= coin:
            numCoins += 1
            total -= coin
    return numCoins if total <= 0 else -1
