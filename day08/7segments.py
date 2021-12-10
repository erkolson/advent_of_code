#!/usr/bin/env python3

#   0:     1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# input = "example-input.txt"
input = "display-input.txt"

outputs = []
inputs = []
with open(input) as fd:
    for line in fd:
        input = line.split('|')[0].strip().split(' ')
        inputs.append(["".join(sorted(word)) for word in input])
        output = line.split('|')[1].strip().split(' ')
        outputs.append(["".join(sorted(word)) for word in output])

count = 0
for word in outputs:
    for digit in word:
        if len(digit) in [ 2, 3, 4, 7]:
            count += 1

print(f"found {count} 1s, 7s, 4 s, and 8s")

def segment_diff(first, second):
    first_list = [i for i in first]
    second_list = [i for i in second]
    diff = []
    for char in first_list:
        if char not in second_list:
            diff.append(char)
    return diff

decoded_outputs = []
for i,input in enumerate(inputs):
    segments = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",0:""}
    six_segments = []
    five_segments = []
    for word in input:
        if len(word) == 2:
            segments[1] = word
        elif len(word) == 3:
            segments[7] = word
        elif len(word) == 4:
            segments[4] = word
        elif len(word) == 7:
            segments[8] = word
        elif len(word) == 6:
            six_segments.append(word)
        elif len(word) == 5:
            five_segments.append(word)

    # find 9, has all of 4's segments
    for word in six_segments:
        if not segment_diff(segments[4], word):
            segments[9] = word
            six_segments.remove(word)

    # find 0, has all of 1's segments
    for word in six_segments:
        if not segment_diff(segments[1], word):
            segments[0] = word
            six_segments.remove(word)

    # six remains
    segments[6] = six_segments[0]

    # find 3, has all of 1's segments
    for word in five_segments:
        if not segment_diff(segments[1], word):
            segments[3] = word
            five_segments.remove(word)

    # find 5, all 5 segments match with 9
    for word in five_segments:
        if not segment_diff(word, segments[9]):
            segments[5] = word
            five_segments.remove(word)

    # 2 remains (also matches 3 of 9's segments)
    segments[2] = five_segments[0]

    digits_lookup = {v: k for k,v in segments.items()}
    decoded = [digits_lookup[digit] for digit in outputs[i]]
    decoded_outputs.append(decoded)

converted = [int("".join([str(digit) for digit in word])) for word in decoded_outputs]
print(converted)
print(sum(converted))
