# Advent of Code - Day 21 - Part One
from functools import cache

def evaluate(jobs, name):
    expression_parts = jobs[name]
    if len(expression_parts) < 2:
        return int(expression_parts[0])
    else:
        return eval(
            str(evaluate(jobs, expression_parts[0]))
            + expression_parts[1]
            + str(evaluate(jobs, expression_parts[2]))
        )
@cache
def result(input):
    lines = [line for line in input.strip().split("\n")]
    monkey_jobs = {}
    for line in lines:
        monkey_jobs[line.split()[0][:-1]] = line.split(":")[1].split()
    root_result = int(evaluate(monkey_jobs, "root"))
    return root_result
