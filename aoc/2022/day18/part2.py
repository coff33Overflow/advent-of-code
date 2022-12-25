# Advent of Code - Day 18 - Part Two
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

    all_droplets = {(x, y, z) for x in range(20) for y in range(20) for z in range(20)}
    empty_droplets = all_droplets - scanned_droplets

    queue = [(0, 0, 0)]
    while len(queue)>0:
        cube = queue.pop()
        if cube in empty_droplets:
            empty_droplets.remove(cube)
            queue.extend(neighbours(cube))
    for empty_droplet in empty_droplets:
        ans += 6
        for adjacent_cube in neighbours(empty_droplet):
            if adjacent_cube in scanned_droplets:
                ans -= 2
        scanned_droplets.add(empty_droplet)
    return ans
