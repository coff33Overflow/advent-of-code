# Advent of Code - Day 25 - Part One
from functools import cache

digits = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
digits_rev = {v: k for k, v in digits.items()}

def SNAFU_to_decimal(s):
    d = 0
    for c in s:
        d = d * 5 + digits[c]
    return d


def decimal_to_SNAFU(n):
    if not n:
        return '0'
    s = ''
    while n:
        n, d = divmod(n, 5)
        if d >= 3:
            d -= 5
            n += 1
        s = digits_rev[d] + s
    return s

@cache
def result(input):
    return decimal_to_SNAFU(sum(SNAFU_to_decimal(i) for i in input.split("\n")))
