#!/usr/bin/env python3

input = "position-input.txt"

initial_positions = []
with open(input) as fd:
    for line in fd:
        initial_positions = [int(loc) for loc in line.split(',')]

# initial_positions = [16,1,2,0,4,2,7,1,2,14]

min_pos = min(initial_positions)
max_pos = max(initial_positions)

print(f"{len(initial_positions)} crabs, arranged from {min_pos} to {max_pos}, sum of positions {sum(initial_positions)}")

def calc_dumb_cost(pos, positions):
    cost = 0
    for position in positions:
        cost += abs(pos - position)
    return cost

def calc_cost(pos, positions):
    cost = 0
    for position in positions:
        distance = abs(pos - position)
        cost += distance*(distance+1)/2
    return cost


# print(f"cost to move all to 500 = {calc_cost(500,initial_positions)}")

for position in range(min_pos, max_pos + 1):
    print(f"cost to move all to {position} = {calc_cost(position,initial_positions)}")
