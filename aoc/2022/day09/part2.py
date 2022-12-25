# Advent of Code - Day 9 - Part Two
from functools import cache
@cache
def result(input):
    dirs = {"U": 1j, "D": -1j, "L": -1, "R": 1}
    sign = lambda a: (a > 0) - (a < 0)
    rope, s2 = [0] * 10, {0}

    for line in input.splitlines():
        d, s = line.split()

        for _ in range(int(s)):
            rope[0] += dirs[d]

            for i in range(1, len(rope)):
                if abs(diff := rope[i - 1] - rope[i]) >= 2:
                    rope[i] += complex(sign(diff.real), sign(diff.imag))

            s2.add(rope[-1])

    return len(s2)

