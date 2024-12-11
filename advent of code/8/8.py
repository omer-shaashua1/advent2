from pathlib import Path
from itertools import combinations

map_input = Path("G:\My Drive\Python Projects\input8.txt").read_text().split()


map_start = []


for i in range(len(map_input)):
    row = []
    for j in range(len(map_input[i])):
        row.append(map_input[i][j])
    map_start.append(row)


antena_location = {}

for line_no in range(len(map_start)):
    for col_no in range(len(map_start[line_no])):
        if map_start[line_no][col_no].isalnum():
            if map_start[line_no][col_no] in antena_location:
                antena_location[map_start[line_no][col_no]].append((line_no, col_no))
            else:
                antena_location[map_start[line_no][col_no]]= [(line_no, col_no)]



antinode_map = map_start.copy()

for freq in antena_location:
    antena_pair = list(combinations(antena_location[freq], 2))
    for pair in antena_pair:
        line_diff = pair[0][0] - pair[1][0]
        col_diff = pair[0][1] - pair[1][1]

        antinode_1_line = pair[0][0] + line_diff
        antinode_1_col = pair[0][1] + col_diff

        if 0 <= antinode_1_line < len(map_start) and 0 <= antinode_1_col < len(map_start[0]):
                antinode_map[pair[0][0]+line_diff][pair[0][1]+col_diff] = "#"
        antinode_2_line = pair[1][0] - line_diff
        antinode_2_col = pair[1][1] - col_diff
        if 0 <= antinode_2_line < len(map_start) and 0 <= antinode_2_col < len(map_start[0]):
                antinode_map[pair[1][0]-line_diff][pair[1][1]-col_diff] = "#"



antinode = 0
for line in antinode_map:
    print(line)
    for col in line:
        if col == "#":
            antinode += 1

print(antinode)