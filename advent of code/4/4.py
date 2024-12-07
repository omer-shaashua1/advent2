from pathlib import Path
import re

input = Path("G:\My Drive\Python Projects\input4.txt").read_text()


input_list = input.split()


def check_diag(input:list, line: int, location: int):
    diag = [""]*4
    count = 0
    try:
        diag[0] = diag[0] + input[line][location] + input[line+1][location+1] + input[line+2][location+2] + input[line+3][location+3]
    except:
        pass
    if location > 2:
        try:
            diag[1] = diag[1] + input[line][location] + input[line+1][location-1] + input[line+2][location-2] + input[line+3][location-3]
        except:
            pass
    if line > 2:
        try:
            diag[2] = diag[2] + input[line][location] + input[line-1][location+1] + input[line-2][location+2] + input[line-3][location+3]
        except:
            pass
    if location > 2 and line > 2:
        try:
            diag[3] = diag[3] + input[line][location] + input[line-1][location-1] + input[line-2][location-2] + input[line-3][location-3]
        except:
            pass
    for idx in diag:
        if idx == "XMAS":
            count = count + 1
    return count


def check_ver(input:list, line: int, location: int):
    vert = ["",""]
    count = 0
    try:
        vert[0] = vert[0] + input[line][location] + input[line+1][location] + input[line+2][location] + input[line+3][location]
    except:
        pass
    if line > 2:
        try:
            vert[1] = vert[1] + input[line][location] + input[line-1][location] + input[line-2][location] + input[line-3][location]
        except:
            pass
    for idx in vert:
        if idx == "XMAS":
            count = count + 1
    return count


def check_hor(input:list, line: int, location: int):
    hor = ["",""]
    count = 0
    try:
        hor[0] = hor[0] + input[line][location] + input[line][location+1] + input[line][location+2] + input[line][location+3]
    except:
        pass
    if location > 2:
        try:
            hor[1] = hor[1] + input[line][location] + input[line][location-1] + input[line][location-2] + input[line][location-3]
        except:
            pass
    for idx in hor:
        if idx == "XMAS":
            count = count + 1
    return count




def check_x_mas(input_A:list, line: int, location: int):
    diag = ["",""]
    count = 0
    if line > 0 and location > 0:
        try:
            diag[0] = input_A[line-1][location-1] + input_A[line][location] + input_A[line+1][location+1]
        except:
            pass
    if line > 0 and location > 0:
        try:
            diag[1] = input_A[line-1][location+1] + input_A[line][location] + input_A[line+1][location-1]
        except:
            pass
    if all(diags == "MAS" or diags == "SAM" for diags in diag):
         count = count + 1
    return count

xmas_no = 0
for line_nu in range(len(input_list)):
    for letter_nu in range(len(input_list[line_nu])):
        if input_list[line_nu][letter_nu] == "X":
            xmas_no = xmas_no + check_diag(input_list, line_nu, letter_nu) + check_hor(input_list, line_nu, letter_nu) + check_ver(input_list, line_nu, letter_nu)


x_mas = 0
for line_nu in range(len(input_list)):
    for letter_nu in range(len(input_list[line_nu])):
        if input_list[line_nu][letter_nu] == "A":
            x_mas = x_mas + check_x_mas(input_list, line_nu, letter_nu) 

print(x_mas)
