#!/usr/bin/env python3

input = "input-map.txt"
topo_map = [[]]
mins = [[]]

with open(input) as fd:
    # print(len(fd.first()))
    map_input = [line.strip() for line in fd.readlines()]
    lines = len(map_input)
    cols = len(map_input[0])

    topo_map = [[0 for i in range(lines+2)] for j in range(cols+2)]
    mins = [[None for i in range(lines)] for j in range(cols)]

    for i,line in enumerate(topo_map):
        for j,point in enumerate(line):
            if i == 0 or j == 0 or i == lines + 1 or j == cols + 1:
                topo_map[i][j] = 10
            else:
                topo_map[i][j] = int(map_input[i-1][j-1])

# print(topo_map)
#      j-1    j    j+1
# i-1  pntA  pntB  pntC
# i    pntD  cur   pntE
# i+1  pntF  pntG  pntH

for i,line in enumerate(topo_map):
    for j,point in enumerate(topo_map):
        cur_point = topo_map[i][j]
        if i == 0 or j == 0 or i == lines + 1 or j == cols + 1:
            pass
        elif cur_point < topo_map[i-1][j] and \
             cur_point < topo_map[i+1][j] and \
             cur_point < topo_map[i][j-1] and \
             cur_point < topo_map[i][j+1]:
             mins[i-1][j-1] = cur_point

print(mins)
risk_sum = 0
for line in mins:
    for point in line:
        if point is not None:
           risk_sum += point + 1

print(f"risk sum = {risk_sum}")

exit(0) # shit don't work yet...

def find_basin(topo, i, j):
    if topo[i][j] < 9:
        # print(f"i={i},j={j}")
        point = [(i,j)]
        # up
        # point.extend( find_basin(topo,i-1,j))
        # right
        point.extend(find_basin(topo,i,j+1))
        # down
        point.extend(find_basin(topo,i+1,j))
        # left
        # point.extend(find_basin(topo,i,j-1))
        return point
    else:
        return []


for i,line in enumerate(topo_map):
    for j,point in enumerate(topo_map):
        if i == 0 or j == 0 or i == lines + 1 or j == cols + 1:
            pass
        basin_from_current_point = find_basin(topo_map,i,j)

        print(basin_from_current_point)
