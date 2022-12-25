# Advent of Code - Day 21 - Part Two
from functools import cache

def evaluate(jobs, name, human_number):
    expression_parts = jobs[name]
    if name == "humn" and human_number >= 0:
        return human_number
    if len(expression_parts) < 2:
        return int(expression_parts[0])
    else:
        return eval(
            str(evaluate(jobs, expression_parts[0], human_number))
            + expression_parts[1]
            + str(evaluate(jobs, expression_parts[2], human_number))
        )
@cache
def result(input):
    lines = [line for line in input.strip().split("\n")]
    monkey_jobs = {}
    for line in lines:
        monkey_jobs[line.split()[0][:-1]] = line.split(":")[1].split()
    root_exp1 = monkey_jobs["root"][0]
    root_exp2 = monkey_jobs["root"][2]

    # one of them isn't dependent on the input, figure out which one, and make sure that's set to root_exp2
    if evaluate(monkey_jobs, root_exp2, 0) != evaluate(monkey_jobs, root_exp2, 1):
        root_exp1, root_exp2 = root_exp2, root_exp1

    # # try it both directions, only one should work and produce an output
    expr1_goal = evaluate(monkey_jobs, root_exp2, 0)

    low = 0
    high = int(1e20)
    try1 = 0
    while low < high and abs(high - low) > 1:
        middle = (low + high) // 2
        current_result = expr1_goal - evaluate(monkey_jobs, root_exp1, middle)
        if current_result < 0:
            low = middle
        elif current_result == 0:
            try1 =  middle
            break
        else:
            high = middle

    low = 0
    high = int(1e20)
    try2 = 0
    while low < high and abs(high - low) > 1:
        middle = (low + high) // 2
        current_result = expr1_goal - evaluate(monkey_jobs, root_exp1, middle)
        if current_result < 0:
            high = middle
        elif current_result == 0:
            try2 = middle
            break
        else:
            low = middle

    if try1 != 0:
        return try1
    else:
        return try2
