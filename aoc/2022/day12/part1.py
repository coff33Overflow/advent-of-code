# Advent of Code - Day 12 - Part One
from functools import cache
def bfs(graph, start, end):
    queue, visited = [[start]], []
    while queue:
        path = queue.pop(0)
        if path[-1][2] == end:
            return len(path) - 1
        for adjacent in graph[path[-1]]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(list(path) + [adjacent])

@cache
def result(input):
    line = input.splitlines()
    cols, rows = len(line[0]), len(line)
    _map = [[ord('a') if c == 'S' else ord('z') if c == 'E' else ord(c) for c in line] for line in line]
    graph = {}

    for r in range(len(line)):
        for c in range(len(line[0])):
            current, n = (r, c, line[r][c]), []
            if current[2] == 'E': end = current
            if r + 1 < rows and _map[r + 1][c] - _map[r][c] >= -1: n.append((r + 1, c, line[r + 1][c]))
            if r - 1 >= 0 and _map[r - 1][c] - _map[r][c] >= -1: n.append((r - 1, c, line[r - 1][c]))
            if c + 1 < cols and _map[r][c + 1] - _map[r][c] >= -1: n.append((r, c + 1, line[r][c + 1]))
            if c - 1 >= 0 and _map[r][c - 1] - _map[r][c] >= -1: n.append((r, c - 1, line[r][c - 1]))
            graph[current] = n

    ans = bfs(graph, end, 'S')

    return ans