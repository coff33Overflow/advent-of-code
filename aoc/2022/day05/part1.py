# Advent of Code - Day 5 - Part One
from functools import cache
import re
from collections import deque
@cache
def result(input):
    initial, instructions = input.split("\n\n")
    initial = initial.split("\n")
    instructions = instructions.strip().split("\n")

    cols: list[deque] = []

    for x in range(max(row.count("[") for row in initial[:-1])):
        col = deque()
        index = x * 4 + 1

        for y in range(len(initial) - 1):
            ch = initial[y][index]
            if ch == " ":
                continue

            col.append(ch)

        cols.append(col)

    for instr in instructions:
        amount, fr, to = map(int, re.findall(r"(\d+)", instr))

        for _ in range(amount):
            cols[to - 1].appendleft(cols[fr - 1].popleft())

    ans = "".join(col[0] for col in cols)
    return ans
