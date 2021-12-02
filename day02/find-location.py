#!/usr/bin/env python3

input = "movement-input.txt"

location = 0
depth = 0

with open(input) as fd:
    for line in fd:
        [direction, amount] = line.split(' ')
        # print(f"heading {direction} for {int(amount)}")
        if direction == "down":
            depth += int(amount)
        elif direction == "up":
            depth -= int(amount)
        elif direction == "forward":
            location += int(amount)
        else:
            print(f"wtf - {direction} {amount}")

print(f"horizontal position is {location} at {depth} depth")
print(f"(horizontal position * depth) = {location*depth}")
