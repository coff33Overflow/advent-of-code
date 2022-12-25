# Advent of Code - Day 16 - Part One
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

    MAX_SCENARIOS = 15000

    loc_data_raw = re.findall(r"Valve (\w\w).*?rate=(\d+).*?valves? (.*)", input)
    rates = dict((loc, int(rate)) for loc, rate, _ in loc_data_raw)
    tunnels = dict(
        (loc, dests.replace(" ", "").split(",")) for loc, _, dests in loc_data_raw
    )

    scenarios = [(0, ["AA"], set())]
    for time in range(1, 31):
        if len(scenarios) > MAX_SCENARIOS:
            scenarios.sort(reverse=True)
            scenarios = scenarios[:MAX_SCENARIOS]
        updated_scenarios = []
        for total_pressure, path, open_valves in scenarios:
            current_loc = path[-1]
            pressure = sum(rates[ov] for ov in open_valves)
            total_pressure += pressure
            for new_path, new_open in get_paths_valves_options(
                tunnels, rates, current_loc, path, open_valves
            ):
                updated_scenarios.append((total_pressure, new_path, new_open))
        scenarios = updated_scenarios
    max_pressure, *_  =  max(scenarios)

    return max_pressure




