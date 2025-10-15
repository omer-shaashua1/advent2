from pathlib import Path
import re

# Create an input for the challenge. Each cell in machines has 3 values - button A, button B and the Prize
# challenge_input = Path("G:\My Drive\Python Projects\input15.txt").read_text().split("\n\n")
challenge_input = Path(r"G:\My Drive\Python Projects\test.txt").read_text().split("\n\n")

regitsters_ABC = challenge_input[0].split("\n")
program = challenge_input[1].split(": ")[1].split(",")
program_int = []
for comm in program:
    program_int.append(int(comm))
print(program_int)
rgstr = [0,1,2,3]

for register in regitsters_ABC:
    split_reg = register.split(": ")
    rgstr.append(int(split_reg[1]))


def adv(registers: list, oprnd: int):
    registers[4] = int(registers[4]/(2**registers[oprnd]))
    return registers


def bxl(registers: list, oprnd: int):
    registers[5] = registers[5]^oprnd
    return registers


def bst(registers: list, oprnd: int):
    registers[5] = registers[oprnd]%8
    return registers

def jnz(registers: list, oprnd: int):
    if registers[4] == 0:
        return False
    else: 
        return str(oprnd)
    

def bxc(registers: list, oprnd: int):
    registers[5] = registers[5]^registers[6]
    return register

def out(registers: list, oprnd: int):
    output = int(registers[oprnd] % 8)
    return output


def bdv(registers: list, oprnd: int):
    registers[5] = int(registers[4]/(2**registers[oprnd]))
    return registers

def cdv(registers: list, oprnd: int):
    registers[6] = int(registers[4]/(2**oprnd))
    return registers


otpt = []
pointer = 0
while pointer <= len(program_int)-2:
    if program_int[pointer] == 0:
        rgstr = adv(rgstr, program_int[pointer+1])
    if program_int[pointer] == 1:
        rgstr = bxl(rgstr, program_int[pointer+1])
    if program_int[pointer] == 2:
        rgstr = bst(rgstr, program_int[pointer+1])
    if program_int[pointer] == 3:
        if jnz(rgstr, program_int[pointer+1]):
            pointer = int(jnz(rgstr, pointer+1)) - 2
    if program_int[pointer] == 4:
        rgstr = bxc(rgstr, pointer+1)
    if program_int[pointer] == 5:
        otpt.append(out(rgstr, program_int[pointer+1]))
    if program_int[pointer] == 6:
        rgstr = bdv(rgstr, program_int[pointer+1])
    if program_int[pointer] == 7:
        rgstr = cdv(rgstr, program_int[pointer+1])
    pointer = pointer + 2 


print(otpt)