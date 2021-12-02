#!/usr/bin/env python3

input_depths = "depths-input.txt"

increases = 0
decreases = 0
unchanged = 0

depths = []

with open(input_depths) as fd:
    for line in fd:
        depths.append(int(line))

windowed_depths = [depths[x] + depths[x+1] + depths[x+2] for x in list(range(0, len(depths) - 2))]

previous_depth = None
for current_depth in windowed_depths:
    if previous_depth is not None:
        if current_depth > previous_depth:
            increases += 1
        elif current_depth < previous_depth:
            decreases += 1
        else:
            unchanged += 1

    previous_depth = current_depth

# print(depths)
# print(windowed_depths)
print(f"{increases} increases, {decreases} decreases, {unchanged} unchanged")
