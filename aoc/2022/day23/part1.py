# Advent of Code - Day 23 - Part One
from functools import cache
from collections import defaultdict

@cache
def result(input):
    elves = set()
    directions = [
        [(-1, -1), (0, -1), (1, -1)],
        [(-1, 1), (0, 1), (1, 1)],
        [(-1, -1), (-1, 0), (-1, 1)],
        [(1, -1), (1, 0), (1, 1)]
    ]

    all_directions = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            all_directions.append((dx, dy))

    for y, line in enumerate(input.splitlines()):
        for x, ch in enumerate(line):
            if ch == "#":
                elves.add((x, y))

    for _ in range(10):
        new_locations = {}
        proposed_counts = defaultdict(int)

        for x, y in elves:
            if all((x + dx, y + dy) not in elves for dx, dy in all_directions):
                new_locations[(x, y)] = (x, y)
                continue

            proposed_cell = None

            for direction in directions:
                if all((x + dx, y + dy) not in elves for dx, dy in direction):
                    proposed_cell = (x + direction[1][0], y + direction[1][1])
                    break

            if proposed_cell is None:
                new_locations[(x, y)] = (x, y)
            else:
                new_locations[(x, y)] = proposed_cell
                proposed_counts[proposed_cell] += 1

        new_elves = set()
        for elf, new_elf in new_locations.items():
            if proposed_counts[new_elf] > 1:
                new_elves.add(elf)
            else:
                new_elves.add(new_elf)

        elves = new_elves
        directions = directions[1:] + [directions[0]]

    ans = 0
    for y in range(min(y for x, y in elves), max(y for x, y in elves) + 1):
        for x in range(min(x for x, y in elves), max(x for x, y in elves) + 1):
            if (x, y) not in elves:
                ans += 1

    return ans
