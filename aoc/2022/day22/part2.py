# Advent of Code - Day 22 - Part Two
from functools import cache
import re
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

            x, y = curr
            if 100 > x >= 50 > y >= 0:
                if face == "U":
                    new_face = "R"
                    new_curr = (0, x + 100)
                elif face == "L":
                    new_face = "R"
                    new_curr = (0, -y + 149)
            elif 100 <= x < 150 and 0 <= y < 50:
                if face == "U":
                    new_face = "U"
                    new_curr = (x - 100, 199)
                elif face == "R":
                    new_face = "L"
                    new_curr = (99, -y + 149)
                elif face == "D":
                    new_face = "L"
                    new_curr = (99, x - 50)
            if 50 <= x < 100 and 50 <= y < 100:
                if face == "L":
                    new_face = "D"
                    new_curr = (y - 50, 100)
                elif face == "R":
                    new_face = "U"
                    new_curr = (y + 50, 49)
            elif 0 <= x < 50 and 100 <= y < 150:
                if face == "L":
                    new_face = "R"
                    new_curr = (50, 149 - y)
                elif face == "U":
                    new_face = "R"
                    new_curr = (50, x + 50)
            elif 50 <= x < 100 <= y < 150:
                if face == "R":
                    new_face = "L"
                    new_curr = (149, 149 - y)
                elif face == "D":
                    new_face = "L"
                    new_curr = (49, x + 100)
            elif 0 <= x < 50 and 150 <= y < 200:
                if face == "L":
                    new_face = "D"
                    new_curr = (y - 100, 0)
                elif face == "R":
                    new_face = "U"
                    new_curr = (y - 100, 149)
                elif face == "D":
                    new_face = "D"
                    new_curr = (x + 100, 0)

            if new_curr in walls:
                break
            curr = new_curr
            face = new_face

        if not turns:
            break

        face = turning[face](turns.pop(0))

    return password(*curr, face)
