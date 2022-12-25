# Advent of Code - Day 2 - Part Two
from functools import cache
@cache
def result(input):
    rds = [r.split(' ') for r in input.splitlines()]

    s = {'X': 1, 'Y': 2, 'Z': 3}
    l, d, w = [['B', 'X'], ['C', 'Y'], ['A', 'Z']], [['A', 'X'], ['B', 'Y'], ['C', 'Z']], [['C', 'X'], ['A', 'Y'], ['B', 'Z']]
    find = lambda i, r: [p[1] for p in i if p[0] == r[0]][0]
    ans = sum([(p + s[find(i, r)]) if r[1] == t else 0 for p, i, t in zip((0, 3, 6), (l, d, w), ('X', 'Y', 'Z')) for r in rds])

    return ans
