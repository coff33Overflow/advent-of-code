# Advent of Code - Day 15 - Part Two
from functools import cache
import re

@cache
def result(input):
    lines = input.strip().split("\n")
    sensors = sorted([[int(a) for a in re.findall(r"-?\d+", l)] for l in lines])
    dist = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)

    s, y = 0, 2_000_000
    for x in range(-1_000_000, 6_000_000):
        for sx, sy, bx, by in sensors:
            if dist(sx, sy, bx, by) >= dist(sx, sy, x, y) and (bx != x or by != y):
                s += 1
                break

    for y in range(4_000_001):
        x = 0
        for sx, sy, bx, by in sensors:
            if dist(sx, sy, bx, by) >= dist(sx, sy, x, y):
                x = sx + dist(sx, sy, bx, by) - abs(sy - y) + 1
        if x <= 4_000_000:
            ans = x * 4_000_000 + y

    return ans
