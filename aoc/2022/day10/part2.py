# Advent of Code - Day 10 - Part Two
from functools import cache
@cache
def result(input):
    x, signal, crt = 1, 0, ""

    for cycle, ins in enumerate(input.split(), start=1):
        signal += cycle * x if cycle % 40 == 20 else 0
        crt += "\u2593" if (cycle - 1) % 40 - x in (-1, 0, 1) else "\u2591"

        if ins[-1].isdigit():
            x += int(ins)

    for i in range(0, len(crt), 40):
        print(crt[i: i + 40])
