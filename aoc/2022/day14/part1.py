# Advent of Code - Day 14 - Part One
from functools import cache
def iterate(cave, endless_void):
    iterations = 0
    while True:
        (sr, sc), sand_moved = [0, 500], True
        while sand_moved:
            sand_moved = True
            if sr + 1 == endless_void + 2:
                sand_moved, cave[sr][sc] = False, "o"
            elif cave[sr + 1][sc] == ".":
                sr += 1
            elif cave[sr + 1][sc - 1] == ".":
                sc -= 1
            elif cave[sr + 1][sc + 1] == ".":
                sc += 1
            else:
                sand_moved, cave[sr][sc] = False, "o"
            if sr > endless_void: return iterations
        iterations += 1

@cache
def result(input):

    lines = input.splitlines()
    cave, endless_void = [["." for _ in range(700)] for _ in range(200)], 0

    for line in lines:
        for s1, s2 in zip(line.split(" -> "), line.split(" -> ")[1:]):
            (x_s1, y_s1), (x_s2, y_s2) = list(map(int, s1.split(","))), list(map(int, s2.split(",")))
            endless_void = max([endless_void, y_s1, y_s2])
            if x_s1 == x_s2:
                for y in range(min(y_s1, y_s2), max(y_s1, y_s2) + 1): cave[y][x_s1] = "#"
            if y_s1 == y_s2:
                for x in range(min(x_s1, x_s2), max(x_s1, x_s2) + 1): cave[y_s1][x] = "#"

    return iterate(cave, endless_void)

