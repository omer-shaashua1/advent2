from pathlib import Path

map_input = Path("G:\My Drive\Python Projects\input6.txt").read_text().split()


map_start = []


for i in range(len(map_input)):
    row = []
    for j in range(len(map_input[i])):
        row.append(map_input[i][j])
    map_start.append(row)


def find_guard(map_func_input):
    for line_no in range(len(map_func_input)):
        for row_no in range(len(map_func_input[line_no])):
            if map_func_input[line_no][row_no] == "^":
                return (line_no, row_no), "^"
            elif map_func_input[line_no][row_no] == ">":
                return (line_no, row_no), ">"
            elif map_func_input[line_no][row_no] == "<":
                return (line_no, row_no), "<"
            elif map_func_input[line_no][row_no] == "V":
                return (line_no, row_no), "V"
    return False
            


def move_up(map_func_input: list):
    if find_guard(map_func_input):
        location, direction = find_guard(map_func_input)
        if location[0]>0: 
            if map_func_input[location[0]-1][location[1]] == "#":
                map_func_input[location[0]][location[1]] = ">"
            else:
                map_func_input[location[0]-1][location[1]] = "^"
                map_func_input[location[0]][location[1]] = "H"
                move_up(map_func_input)
        else:
             map_func_input[location[0]][location[1]] = "H"
        return map_func_input
    else:
        return False

def move_down(map_func_input: list):
    if find_guard(map_func_input):
        location, direction = find_guard(map_func_input)
        try: 
            if map_func_input[location[0]+1][location[1]] == "#":
                map_func_input[location[0]][location[1]] = "<"
            else:
                map_func_input[location[0]+1][location[1]] = "V"
                map_func_input[location[0]][location[1]] = "H"
                move_down(map_func_input)
        except:
            map_func_input[location[0]][location[1]] = "H"
        return map_func_input
    else:
        return False


def move_left(map_func_input: list):
    if find_guard(map_func_input):
        location, direction = find_guard(map_func_input)
        if location[0]>0: 
            if map_func_input[location[0]][location[1]-1] == "#":
                map_func_input[location[0]][location[1]] = "^"
            else:
                map_func_input[location[0]][location[1]-1] = "<"
                map_func_input[location[0]][location[1]] = "H"
                move_left(map_func_input)
        else:
             map_func_input[location[0]][location[1]] = "H"
        return map_func_input
    else:
        return False
    

def move_right(map_func_input: list):
    if find_guard(map_func_input):
        location, direction = find_guard(map_func_input)
        try: 
            if map_func_input[location[0]][location[1]+1] == "#":
                map_func_input[location[0]][location[1]] = "V"
            else:
                map_func_input[location[0]][location[1]+1] = ">"
                map_func_input[location[0]][location[1]] = "H"
                move_right(map_func_input)
        except:
            map_func_input[location[0]][location[1]] = "H"
        return map_func_input
    else:
        return False
    

def make_position_map(map_func_input: list):
    if find_guard(map_func_input):
        location, direction = find_guard(map_func_input)
        if direction == '^':
            pos_map = move_up(map_func_input)
            make_position_map(pos_map)
        elif direction == '>':
            pos_map = move_right(map_func_input)
            make_position_map(pos_map)
        elif direction == 'V':
            pos_map = move_down(map_func_input)
            make_position_map(pos_map)
        elif direction == '<':
            pos_map = move_left(map_func_input)
            make_position_map(pos_map)
    return map_func_input
    

test_map = make_position_map(map_start)



position_number = 0


for line in make_position_map(map_start):
    print(line)
    for col in line:
        if col == 'H':
            position_number += 1


print(position_number)
# print(find_guard(map_start))