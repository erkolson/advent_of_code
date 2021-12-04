#!/usr/bin/env python3

input = "diagnostic-input.txt"

lines = []
with open(input) as fd:
    lines = [line.strip() for line in fd]

oxygen = lines.copy()
co2 = lines.copy()

print(lines)

def drop_some(index, input, oxy=True):
    if len(input) == 1:
        return input
    one_list = []
    zed_list = []
    for line in input:
        if int(line[index]) == 1:
            one_list.append(line)
        else:
            zed_list.append(line)
    if oxy:
        if len(one_list) >= len(zed_list):
            return one_list
        else:
            return zed_list
    else:
        if len(one_list) >= len(zed_list):
            return zed_list
        else:
            return one_list

def binaryizer(zed_one_str):
    zed_one_list = list(zed_one_str)
    zed_one_list.reverse()
    num = 0
    for i in range(0, len(zed_one_list)):
        num += int(zed_one_list[i]) * pow(2, i)
        print(f"i = {i}, num = {num}")
    return num

for i in range(0, len(lines[0])):
    oxygen = drop_some(i, oxygen)
    co2 = drop_some(i, co2, False)

print(oxygen)
print(co2)

oxygen_rating = binaryizer(oxygen[0])
co2_rating = binaryizer(co2[0])

life_support_rating = oxygen_rating * co2_rating

print(f"life support rating = {life_support_rating}")
