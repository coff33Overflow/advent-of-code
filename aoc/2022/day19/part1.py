# Advent of Code - Day day19 - Part One
from functools import cache
import re

def parse_input(data):
	input = []
	lines = [x for x in data.split('\n')]
	parsed_numbers = sorted([[int(a) for a in re.findall(r"-?\d+", l)] for l in lines])
	for numbers_array in parsed_numbers:
		input.append(tuple(numbers_array[1:]))
	return input

def buildtime(cost, available, bots):
	if available >= cost:
		return 1
	else:
		return ((cost - available) + bots-1) // bots + 1

def maximise(bp, time):
	orebot_cost, claybot_cost, obsbot_cost_ore, obsbot_cost_clay, geodebot_cost_ore, geodebot_cost_obs = bp
	maxorebots = max(orebot_cost, claybot_cost, obsbot_cost_ore, geodebot_cost_ore)
	def walk(n, ore, clay, obs, geode, orebot, claybot, obsbot, geodebot):
		yield geode + n * geodebot

		if orebot < maxorebots:
			bt = buildtime(orebot_cost, ore, orebot)
			if n >= bt:
				yield from walk(n - bt, ore + bt*orebot - orebot_cost, clay + bt*claybot, obs + bt*obsbot, geode + bt*geodebot, orebot + 1, claybot, obsbot, geodebot)

		if claybot < obsbot_cost_clay:
			bt = buildtime(claybot_cost, ore, orebot)
			if n >= bt:
				yield from walk(n - bt, ore + bt*orebot - claybot_cost, clay + bt*claybot, obs + bt*obsbot, geode + bt*geodebot, orebot, claybot + 1, obsbot, geodebot)

		if claybot > 0 and obsbot < geodebot_cost_obs:
			bt = max(buildtime(obsbot_cost_ore, ore, orebot), buildtime(obsbot_cost_clay, clay, claybot))
			if n >= bt:
				yield from walk(n - bt, ore + bt*orebot - obsbot_cost_ore, clay + bt*claybot - obsbot_cost_clay, obs + bt*obsbot, geode + bt*geodebot, orebot, claybot, obsbot + 1, geodebot)

		if obsbot > 0:
			bt = max(buildtime(geodebot_cost_ore, ore, orebot), buildtime(geodebot_cost_obs, obs, obsbot))
			if n >= bt:
				yield from walk(n - bt, ore + bt*orebot - geodebot_cost_ore, clay + bt*claybot, obs + bt*obsbot - geodebot_cost_obs, geode + bt*geodebot, orebot, claybot, obsbot, geodebot + 1)

	return max(walk(time, 0, 0, 0, 0, 1, 0, 0, 0))
@cache
def result(input):
	dat = parse_input(input)
	tot = 0
	for i, bp in enumerate(dat, 1):
		res = maximise(bp, 24)
		tot += i * res
	return tot
