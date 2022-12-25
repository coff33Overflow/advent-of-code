#!/usr/bin/env python3
import sys
sys.path.append('../../utils')
sys.dont_write_bytecode = True
import part1, part2, aoc_utils

def main():
    input = open("input.txt").read()

    print("--- Part One ---")
    print("Result:", part1.result(input))
    aoc_utils.submit(part1.result(input), 1, $year, $day)

    print("--- Part Two ---")
    print("Result:", part2.result(input))
    aoc_utils.submit(part2.result(input), 2, $year, $day)

if __name__ == "__main__":
    main()
