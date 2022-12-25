# Advent of Code - Day day20 - Part One
from functools import cache

def max_numbers_sum(values, n):
    values = list(enumerate(values))
    for _ in range(n):
        for i in range(len(values)):
            for k, (j, v) in enumerate(values):
                if j == i:
                    values.pop(k)
                    values.insert((k + v) % len(values), (i, v))
                    break
    values = [v for _, v in values]
    zero = values.index(0)
    return sum(values[(zero + offset) % len(values)] for offset in (1000, 2000, 3000))
@cache
def result(input):
    lines = [int(x) for x in input.strip().split('\n')]
    ans = max_numbers_sum(lines, n=1)
    return ans
