import numpy as np
from pathlib import Path
import re

# Create an input for the challenge. Each cell in machines has 3 values - button A, button B and the Prize
Claw_moves = Path("G:\My Drive\Python Projects\input13.txt").read_text().split("\n")
# Claw_moves = Path(r"G:\My Drive\Python Projects\test.txt").read_text().split("\n")
Machines = []
x = 0
while x < len(Claw_moves)/4:
    Machines.append([])
    i=0
    while i <= 2:
        Machines[x].append(Claw_moves[4*x+i])
        i = i+1
    x = x+1

# print(Machines[1][2].split()[1][2::].strip(","))
# test = []
# test.append(Machines[0][0]

cost = 0

for machine in Machines:
    A_button = []
    B_button = []
    prize = []
    buttons = [[], []]
    i = 0
    while i<2:
        buttons[0].append(int(machine[i].split()[2][2:-1]))
        buttons[1].append(int(machine[i].split()[3][2::]))
        prize.append(int(machine[2].split()[i+1][2::].strip(","))+10000000000000)
        i = i+1
    print(prize)
    Numbers_of_press = np.dot(np.linalg.inv(buttons), prize)
    # print(Numbers_of_press[0])
    if round(Numbers_of_press[0], 3) % 1 == 0 and round(Numbers_of_press[1], 3) % 1 == 0:
        cost = cost + 3*Numbers_of_press[0] + Numbers_of_press[1]
print(cost)

    

# A = [[94 , 22], [34, 67]]
# b = [8400, 5400]
# x = np.dot(np.linalg.inv(A), b)
# print(round(x[1],6) == int(x[1]))

# a = ["Button B: X+19, Y+93"]
# x = re.findall(r"\bX\+", a[0])
# print(x)