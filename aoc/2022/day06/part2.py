# Advent of Code - Day 6 - Part Two
from functools import cache
@cache
def result(input):
    for i in range(14, len(input.strip())):
        if len(set(input[i-14:i])) == 14:
            return i
