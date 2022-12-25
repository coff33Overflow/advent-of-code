# Advent of Code - Day 3 - Part One
from functools import cache
@cache
def result(input):
    d, c = input.splitlines(), 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = sum([c.index(''.join(set.intersection(set(l[:len(l)//2]), l[len(l)//2:])))+1 for l in d])
    return ans
