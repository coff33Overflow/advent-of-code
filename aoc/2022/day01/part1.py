# Advent of Code - Day 1 - Part One
from functools import cache
@cache
def result(input):
    max_calories = 0
    for bags in input.split("\n\n"):
        calories = sum(map(int, bags.split()))
        max_calories = max(max_calories, calories)
    return max_calories
