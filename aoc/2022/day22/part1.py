# Advent of Code - Day 22 - Part One
from functools import cache
import re

def wrap(tile, tiles, face, walls):
    if face == "R":
        return min((x, y) for x, y in tiles | walls if y == tile[1])
    if face == "L":
        return max((x, y) for x, y in tiles | walls if y == tile[1])
    if face == "U":
        return max([(x, y) for x, y in tiles | walls if x == tile[0]], key=lambda x: (x[1], x[0]))
    if face == "D":
        return min([(x, y) for x, y in tiles | walls if x == tile[0]], key=lambda x: (x[1], x[0]))
def peek(x, y, dx, dy):
    return x + dx, y + dy
def password(col, row, face):
    return 1000 * (row + 1) + 4 * (col + 1) + "RDLU".find(face)
@cache
def result(input):
    board, dirs = input.split("\n\n")
    walls = set()
    tiles = set()
    for y, row in enumerate(board.split("\n")):
        for x, cell in enumerate(row):
            match cell:
                case ".":
                    tiles.add((x, y))
                case "#":
                    walls.add((x, y))

    start = min(tiles, key=lambda x: (x[1], x[0]))
    pathnumbers = [int(n) for n in re.findall(r"\d+", dirs)]
    turns = re.findall(r"[RL]", dirs)
    turning = {
        "L": lambda x: "D" if x == "L" else "U",
        "R": lambda x: "U" if x == "L" else "D",
        "D": lambda x: "R" if x == "L" else "L",
        "U": lambda x: "L" if x == "L" else "R"
    }
    moves = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, -1),
        "D": (0, 1)
    }
    face = "R"
    curr = start
    while True:
        steps = pathnumbers.pop(0)
        for step in range(steps):
            temp = peek(*curr, *moves[face])
            if temp in walls:
                break
            if temp in tiles:
                curr = temp
                continue
            new_curr = wrap(temp, tiles, face, walls)
            if new_curr in walls:
                break
            curr = new_curr
        if not turns:
            break
        face = turning[face](turns.pop(0))
    return password(*curr, face)




