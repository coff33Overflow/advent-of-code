# Advent of Code - Day 4 - Part Two
from functools import cache
@cache
def result(input):
    lines = [[list(map(int, d.split('-'))) for d in l.split(',')] for l in input.splitlines()]
    ans = 0

    for line in lines:
        sets = [set(range(l[0], l[1] + 1)) for l in line]
        inter = len(set.intersection(*sets))
        ans += inter > 0
    return ans
