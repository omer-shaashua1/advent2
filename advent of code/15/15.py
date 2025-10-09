from pathlib import Path
import re

# Create an input for the challenge. Each cell in machines has 3 values - button A, button B and the Prize
# challenge_input = Path("G:\My Drive\Python Projects\input15.txt").read_text().split("\n")
challenge_input = Path(r"G:\My Drive\Python Projects\test.txt").read_text().split("\n\n")

map_start = []
map_start.append(challenge_input[0])
challenge_input[1] = challenge_input[1].split("\n")
map_start = map_start[0].split("\n")


movements = ""
for line in challenge_input[1]:
    movements = movements + line


movements_list = []
for move in range(len(movements)):
    movements_list.append(movements[move])

for line in range(len(map_start)):
    map_start[line] = re.findall('.', map_start[line])
    

def find_bot(map: list):
    for line_no in range(len(map)):
        for row_no in range(len(map[line_no])):
            if map[line_no][row_no] == "@":
                return (line_no, row_no)
    return False

for line in map_start:
    print(line)

def check_block(coords: tuple, map_in: list, move: str):
    if move == "<":
        if map_in[coords[0]][coords[1]-1] == '.':
            empty_spot = (coords[0],coords[1]-1)
            return empty_spot
        if map_in[coords[0]][coords[1]-1] == '#':
            return False
        if map_in[coords[0]][coords[1]-1] == 'O':
                next_check = (coords[0], coords[1]-1)
                result = check_block(next_check, map_in, move)
                return result
    if move == ">":
        if map_in[coords[0]][coords[1]+1] == '.':
            empty_spot = (coords[0],coords[1]+1)
            return empty_spot
        if map_in[coords[0]][coords[1]+1] == '#':
            return False
        if map_in[coords[0]][coords[1]+1] == 'O':
                next_check = (coords[0], coords[1]+1)
                result = check_block(next_check, map_in, move)
                return result
    if move == "^":
        if map_in[coords[0]-1][coords[1]] == '.':
            empty_spot = (coords[0]-1,coords[1])
            return empty_spot
        if map_in[coords[0]-1][coords[1]] == '#':
            return False
        if map_in[coords[0]-1][coords[1]] == 'O':
                next_check = (coords[0]-1, coords[1])
                result = check_block(next_check, map_in, move)
                return result
    if move == "v":
        if map_in[coords[0]+1][coords[1]] == '.':
            empty_spot = (coords[0]+1,coords[1])
            return empty_spot
        if map_in[coords[0]+1][coords[1]] == '#':
            return False
        if map_in[coords[0]+1][coords[1]] == 'O':
                next_check = (coords[0]+1, coords[1])
                result = check_block(next_check, map_in, move)
                return result


def make_move(coords: tuple, map_in: list, move: str):
    empty_spot = check_block(coords, map_in, move)
    map_after_move = []
    for line in map_in:
        map_after_move.append(line)
    map_after_move[coords[0]][coords[1]] = "."
    map_after_move[empty_spot[0]][empty_spot[1]] = "O"
    if move == "<":
         map_after_move[coords[0]][coords[1]-1] = "@"
    if move == ">":
         map_after_move[coords[0]][coords[1]+1] = "@"
    if move == "^":
         map_after_move[coords[0]-1][coords[1]] = "@"
    if move == "v":
         map_after_move[coords[0]+1][coords[1]] = "@"
    return map_after_move     


output = map_start

for move in movements_list:
    try:
        output = make_move((4,4), output, move)
    except:
         pass
print("************")
for line in output:
     print(line)
    
     

