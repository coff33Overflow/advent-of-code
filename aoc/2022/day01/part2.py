# Advent of Code - Day 1 - Part Two
from functools import cache
@cache
def result(input):
    max_3_calories = []
    for bags in input.split("\n\n"):
        calories = sum(map(int, bags.split()))
        max_3_calories.append(calories)
        max_3_calories.sort()
    return sum(max_3_calories[-3:])