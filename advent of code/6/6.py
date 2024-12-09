from pathlib import Path

map_input = Path("G:\My Drive\Python Projects\input6.txt").read_text().split()


map_start = []


for i in range(len(map_input)):
    row = []
    for j in range(len(map_input[i])):
        row.append(map_input[i][j])
    map_start.append(row)




print(map_start)