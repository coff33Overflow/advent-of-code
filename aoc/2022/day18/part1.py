# Advent of Code - Day 18 - Part One
from functools import cache
def neighbours(cube):
    x, y, z = cube
    yield x + 1, y, z
    yield x - 1, y, z
    yield x, y + 1, z
    yield x, y - 1, z
    yield x, y, z + 1
    yield x, y, z - 1
@cache
def result(input):
    ans = 0
    droplets = [tuple(map(int, line.split(","))) for line in input.splitlines()]
    scanned_droplets = set()

    for droplet in droplets:
        ans += 6
        for adjacent_cube in neighbours(droplet):
            if adjacent_cube in scanned_droplets:
                ans -= 2
        scanned_droplets.add(droplet)
    return ans
