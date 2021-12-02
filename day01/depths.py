#!/usr/bin/env python3

input_depths = "depths-input.txt"

increases = 0
decreases = 0
unchanged = 0

with open(input_depths) as fd:
    previous_line = None
    current_line = None
    for line in fd:
        current_line = int(line)
        if previous_line is not None:
            if current_line > previous_line:
                increases += 1
            elif current_line < previous_line:
                decreases += 1
            else:
                unchanged += 1
        print(f"current_line = {current_line}")
        previous_line = current_line

print(f"{increases} increases, {decreases} decreases, {unchanged} unchanged")
