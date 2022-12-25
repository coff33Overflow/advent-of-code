# Advent of Code - Day 8 - Part Two
from functools import cache
from numpy import *
@cache
def result(input):
    trees = array([[int(d) for d in line] for line in input.splitlines()])
    rows, cols = shape(trees)
    visible_count = scenic_score = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            tree, directions = trees[r, c], (
            flip(trees[0:r, c]), trees[r + 1:, c], flip(trees[r, 0:c]), trees[r, c + 1:])
            visible_count += any([all(tree > direction) for direction in directions])
            counts = [argmax(view >= tree) + 1 if any(view >= tree) else view.size for view in directions]
            scenic_score = max(scenic_score, counts[0] * counts[1] * counts[2] * counts[3])

    return scenic_score
