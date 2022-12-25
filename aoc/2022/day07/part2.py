# Advent of Code - Day 7 - Part Two
from functools import cache
from collections import defaultdict
@cache
def result(input):
    cwd = []
    sizes = defaultdict(int)

    for line in input.strip().split("\n"):
        if "$ cd" in line:
            _, cmd, dir = line.split(" ")
            if dir == "..":
                cwd = cwd[:-1]
            else:
                cwd.append(dir)

        elif "$ ls" in line:
            continue
        else:
            sz, name = line.split()
            if (
                    sz.isnumeric()
            ):
                for i in range(1, len(cwd) + 1):
                    sizes["/".join(cwd[0:i])] += int(sz)

    for sz in sorted(sizes.values()):
        if sizes["/"] - sz <= 40000000:
            ans = sz
            break
    return ans
