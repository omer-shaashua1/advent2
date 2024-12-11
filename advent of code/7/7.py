from pathlib import Path
from itertools import product


cal_input = Path("G:\My Drive\Python Projects\input7.txt").read_text().split("\n")
cal_list = []
for cal in cal_input:
    cal_list.append(cal.split(":"))

for cal in range(len(cal_list)):
    cal_list[cal][1] = cal_list[cal][1].split()


def get_result(factors: list, ops: list):
    result = factors[0]
    for idx, op in enumerate(ops):
        if op == "+":
            result += factors[idx+1]
        elif op == "*":
            result *= factors[idx+1]
        elif op == '||':
            result = int(str(result)+str(factors[idx+1]))
    return result


def is_solvable(target: int, factors: list):
    operators_no = len(factors)-1
    for ops in list(product(['+','*','||'], repeat=operators_no)):
        if get_result(factors, ops) == target:
            return True
    return False
    
solvable = 0

for cal in cal_list:
    factors = []
    wanted_result = int(cal[0])
    for factor in cal[1]:
        factors.append(int(factor))
    if is_solvable(wanted_result, factors):
        solvable += wanted_result


print(solvable)
