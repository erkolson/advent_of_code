#!/usr/bin/env python3

input = "line-inputs.txt"

def parse_line_segment(input_str):
    segment = [point.strip().split(',') for point in input_str.split('->')]
    return [[int(coordinate) for coordinate in point] for point in segment]

line_segments = []
with open(input) as fd:
    for line_segment in fd:
        line_segments.append(parse_line_segment(line_segment))

def vertical(segment):
    if segment[0][0] == segment[1][0]:
        return True
    else:
        return False

def horizontal(segment):
    if segment[0][1] == segment[1][1]:
        return True
    else:
        return False

class MapMatrix:
    diagram = [[]]
    size = 0
    def __init__(self,size):
        self.size = size
        self.diagram = [[0 for i in range(self.size + 1)] for j in range(self.size + 1)]

    def __str__(self):
        str = ""
        for i in range(0,self.size):
            for j in range(0,self.size):
                str += f"{self.diagram[i][j]} "
            str += "\n"
        return str

    def draw_vert_line(self, segment):
        y1 = segment[0][1]
        y2 = segment[1][1]
        x = segment[0][0]
        modifier = 1 if y2 > y1 else -1
        for j in range(y1, y2 + modifier, modifier):
            # print("adding vert point")
            self.diagram[x][j] += 1

    def draw_horiz_line(self, segment):
        x1 = segment[0][0]
        x2 = segment[1][0]
        y = segment[0][1]
        # print(f"x1={x1},x2={x2},y={y}")
        modifier = 1 if x2 > x1 else -1
        for i in range(x1, x2 + modifier, modifier):
            # print("adding horiz point")
            self.diagram[i][y] += 1

    def draw_diagonal(self, segment):
        y1 = segment[0][1]
        y2 = segment[1][1]
        x1 = segment[0][0]
        x2 = segment[1][0]
        x_modifier = 1 if x2 > x1 else -1
        y_modifier = 1 if y2 > y1 else -1
        for x,i in enumerate(range(x1, x2 + x_modifier, x_modifier)):
            for y,j in enumerate(range(y1, y2 + y_modifier, y_modifier)):
                # print(f"x={x},i={i},y={y},j={j}")
                if x == y:
                    self.diagram[i][j] += 1

    def intersections(self):
        points = 0
        for i in range(0,self.size):
            for j in range(0,self.size):
                if self.diagram[i][j] > 1:
                    points += 1
        return points


# print(line_segments)
max_coordinate = max([coordinate for segment in line_segments for point in segment for coordinate in point])
print(f"max coordinate={max_coordinate}")
sea_map = MapMatrix(max_coordinate)
sea_map_diag = MapMatrix(max_coordinate)
# no_diagonal_segments = [segment for segment in line_segments if horizontal(segment) or vertical(segment)]

for segment in line_segments:
    if horizontal(segment):
        # print(f"horizontal segment {segment}")
        sea_map.draw_horiz_line(segment)
        sea_map_diag.draw_horiz_line(segment)
    elif vertical(segment):
        # print(f"vertical segment {segment}")
        sea_map.draw_vert_line(segment)
        sea_map_diag.draw_vert_line(segment)
    else:
        # print(f"diagonal segment {segment}")
        sea_map_diag.draw_diagonal(segment)

# print(sea_map)
intersections = sea_map.intersections()
print(f"horiz/vert only line intersections = {intersections}")
intersections_diag = sea_map_diag.intersections()
print(f"total line intersections = {intersections_diag}")
