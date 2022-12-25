# Advent of Code - Day 3 - Part Two
from functools import cache
@cache
def result(input):
    d, c = input.splitlines(), 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = sum([c.index(''.join(set.intersection(set(d[i]), d[i+1], d[i+2])))+1 for i in range(0, len(d)-2, 3)])
    return ans
