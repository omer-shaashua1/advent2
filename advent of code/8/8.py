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

antena_pair = list(combinations(antena_location["A"], 2))

for freq in antena_location:
    antena_pair = list(combinations(antena_location[freq], 2))
    for pair in antena_pair:
        line_diff = pair[0][0] - pair[1][0]
        row_diff = pair[0][1] - pair[1][1]
        print(freq, pair, line_diff, row_diff)
        if pair[0][0]+line_diff >= 0 and pair[0][1]+row_diff >= 0:
            try:
                map_start[pair[0][0]+line_diff][pair[0][1]+row_diff] = "#"
            except:
                pass
        if pair[1][0]+line_diff >= 0 and pair[1][1]+row_diff >= 0:
            try:
                map_start[pair[1][0]-line_diff][pair[1][1]-row_diff] = "#"
            except:
                pass


antinode = 0
for line in map_start:
    # print(line)
    for col in line:
        if col == "#":
            antinode += 1

print(antinode)