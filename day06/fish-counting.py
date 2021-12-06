#!/usr/bin/env python3

input = "fish-input.txt"
days = 256

initial_ages = []
with open(input) as fd:
    for line in fd:
        initial_ages = [int(age) for age in line.split(',')]

fish_map = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
for fish in initial_ages:
    fish_map[fish] += 1

def school_state(tha_fish_map):
    print(f"{{age:count}} {tha_fish_map} fish, {sum(tha_fish_map.values())} total")

print("Starting With:")
school_state(fish_map)

for day in range(1,days + 1):
    new_fish_map = {}
    new_fish_map[8] = fish_map[0]
    new_fish_map[7] = fish_map[8]
    new_fish_map[6] = fish_map[0] + fish_map[7]
    new_fish_map[5] = fish_map[6]
    new_fish_map[4] = fish_map[5]
    new_fish_map[3] = fish_map[4]
    new_fish_map[2] = fish_map[3]
    new_fish_map[1] = fish_map[2]
    new_fish_map[0] = fish_map[1]

    fish_map = new_fish_map.copy()
    print(f"After day {day}:")
    school_state(new_fish_map)
