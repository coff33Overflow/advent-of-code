# Advent of Code - Day 2 - Part One
from functools import cache
@cache
def result(input):
    rds = [r.split(' ') for r in input.splitlines()]

    s = {'X': 1, 'Y': 2, 'Z': 3}
    l, d, w = [['B', 'X'], ['C', 'Y'], ['A', 'Z']], [['A', 'X'], ['B', 'Y'], ['C', 'Z']], [['C', 'X'], ['A', 'Y'],  ['B', 'Z']]
    ans = sum([(p + s[r[1]]) if r in i else 0 for p, i in zip((0, 3, 6), (l, d, w)) for r in rds])

    return ans

