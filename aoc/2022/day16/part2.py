# Advent of Code - Day 16 - Part Two
from functools import cache
import re

def get_paths_valves_options(tunnels, flow_rate, curr_location, path, open_valves):
    res = []
    for loc in tunnels[curr_location]:
        res.append((path + [loc], open_valves.copy()))
    if flow_rate[curr_location] > 0 and curr_location not in open_valves:
        res.append((path, open_valves | {curr_location}))
    return res
@cache
def result(input):

    MAX_SCENARIOS = 15000 # 10k wasn't enough for part2 ... wrong answer

    loc_data_raw = re.findall(r"Valve (\w\w).*?rate=(\d+).*?valves? (.*)", input)
    rates = dict((loc, int(rate)) for loc, rate, _ in loc_data_raw)
    tunnels = dict(
        (loc, dests.replace(" ", "").split(",")) for loc, _, dests in loc_data_raw
    )

    scenarios = [(0, (["AA"], ["AA"]), set())]
    for time in range(1, 27):
        if len(scenarios) > MAX_SCENARIOS:
            scenarios.sort(reverse=True)
            scenarios = scenarios[:MAX_SCENARIOS]
        updated_scenarios = []
        for total_pressure, path, open_valves in scenarios:
            me_loc = path[0][-1]
            ele_loc = path[1][-1]
            pressure = sum(rates[ov] for ov in open_valves)
            total_pressure += pressure
            for new_path_me, new_open_me in get_paths_valves_options(
                    tunnels, rates, me_loc, path[0], open_valves
            ):
                for new_path_ele, new_open_ele in get_paths_valves_options(
                        tunnels, rates, ele_loc, path[1], new_open_me
                ):
                    updated_scenarios.append(
                        (total_pressure, (new_path_me, new_path_ele), new_open_ele)
                    )
        scenarios = updated_scenarios
    pressure, *_ =  max(scenarios)

    return pressure





