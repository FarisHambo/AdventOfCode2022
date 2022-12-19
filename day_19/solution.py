import re
import sys
from functools import cache

with open("/Users/farishambo/Desktop/advent_git/AdventOfCode2022/day_19/input.txt") as f:
    blueprints = []
    for blueprint in f.read().strip().splitlines():
        costs = list(map(int, re.findall(r"\d+", blueprint)))
        blueprints.append(tuple(costs[1:]))

sys.setrecursionlimit(100000000) 


@cache
def DFS(robots, resources, time, blueprint, building) -> int:
    resources = list(resources)  
    time -= 1
    if time == 0:
        return resources[3]
    resources = [resources[i] + robots[i] for i in range(4)]

    if building != -1:
        robots = list(robots)
        robots[building] += 1
        robots = tuple(robots)
        building = -1

    solution = DFS(robots, tuple(resources), time, blueprint, -1)

    if resources[0] >= blueprint[0]:
        new = resources.copy()
        new[0] -= blueprint[0]
        solution = max(DFS(robots, tuple(new), time, blueprint, 0), solution)

    if resources[0] >= blueprint[1]:
        new = resources.copy()
        new[0] -= blueprint[1]
        solution = max(DFS(robots, tuple(new), time, blueprint, 1), solution)

    if resources[0] >= blueprint[2] and resources[1] >= blueprint[3]:
        new = resources.copy()
        new[0] -= blueprint[2]
        new[1] -= blueprint[3]
        solution = max(DFS(robots, tuple(new), time, blueprint, 2), solution)

    if resources[0] >= blueprint[4] and resources[2] >= blueprint[5]:
        new = resources.copy()
        new[0] -= blueprint[4]
        new[2] -= blueprint[5]
        solution = max(DFS(robots, tuple(new), time, blueprint, 3), solution)

    return solution


P1 = 0
P2 = 1
for i, blueprint in enumerate(blueprints):
    print(i)
    if i < 3:
        P2 *= DFS((1, 0, 0, 0), (0, 0, 0, 0), 32, blueprint, -1)
print(P2)
for i, blueprint in enumerate(blueprints):
    print(i)
    P1 += (i + 1) * DFS((1, 0, 0, 0), (0, 0, 0, 0), 24, blueprint, -1)
print(P1)

print(P1, P2)