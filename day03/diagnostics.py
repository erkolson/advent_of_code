#!/usr/bin/env python3

input = "diagnostic-input.txt"

gamma_rate = 0
epsilon_rate = 0
lines = []

with open(input) as fd:
    lines = [line.strip() for line in fd]

accumulator = [0 for i in range(len(lines[0]))]

for line in lines:
    for i, sample in enumerate(list(line)):
        if int(sample) > 0:
            accumulator[i] += 1
        else:
            accumulator[i] -= 1

# print(accumulator)
gamma = []
epsilon = []
for digit in accumulator:
    if digit > 0:
        gamma.append(1)
        epsilon.append(0)
    elif digit < 0:
        gamma.append(0)
        epsilon.append(1)
    else:
        print("undefined bro!")

# print(gamma)
# print(epsilon)

gamma.reverse()
epsilon.reverse()
gamma_rate = 0
epsilon_rate = 0

for i in range(0,len(gamma)):
    gamma_rate += gamma[i] * pow(2,i)
    epsilon_rate += epsilon[i] * pow(2,i)

power = gamma_rate * epsilon_rate

print(f"gama rate = {gamma_rate}, epsilon rate = {epsilon_rate}, power consumption is {power}")
