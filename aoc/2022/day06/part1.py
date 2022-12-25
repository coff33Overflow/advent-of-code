# Advent of Code - Day 6 - Part One
from functools import cache
@cache
def result(input):
    for i in range(4, len(input.strip())):
        if len(set(input[i-4:i])) == 4:
            return i
