# Advent of Code - Day 24 - Part One
from functools import cache
from collections import deque

def has_blizzard(grid, N, M, t, i, j):
    if (i, j) in ((-1, 0), (N, M - 1)):
        return False
    try:
        return (
                grid[(i - t) % N, j] == "v"
                or grid[(i + t) % N, j] == "^"
                or grid[i, (j - t) % M] == ">"
                or grid[i, (j + t) % M] == "<"
        )
    except KeyError:
        return True

def shortest(grid, N, M, start, end, start_t=0):
    DIRECTIONS = [(1, 0, 0), (1, -1, 0), (1, 1, 0), (1, 0, -1), (1, 0, 1)]
    visited = set()
    bfs = deque([(start_t, *start)])

    while len(bfs) > 0:
        t, i, j = p = bfs.popleft()
        if p in visited:
            continue
        visited.add(p)

        if (i, j) == end:
            return t

        for d in DIRECTIONS:
            x = tuple(sum(i) for i in zip(p, d))
            if not has_blizzard(grid, N, M, *x):
                bfs.append(x)

@cache
def result(input):

    lines = [row[1:-1] for row in input.splitlines()[1:-1]]
    grid = {(i, j): cell for i, row in enumerate(lines) for j, cell in enumerate(row)}
    N, M = len(lines), len(lines[0])
    grid[-1, 0] = grid[N, M - 1] = "."
    return shortest(grid, N, M, (-1, 0), (N, M - 1))