from pathlib import Path
import re

input = Path("G:\My Drive\Python Projects\input3.txt").read_text()



pattern = r"(mul\(\d+,\d+\)|don't\(\)|do\(\))"

ops = re.findall(pattern, input)


commands_active = True

sum_of_mults = 0
for op in ops:
    if op == "do()":
        commands_active = True
    elif op == "don't()":
        commands_active = False
    else:
        if commands_active:
            op = op[4:-1]
            pair = op.split(",")
            mult = int(pair[0]) * int(pair[1])
            sum_of_mults = sum_of_mults + mult
print(sum_of_mults)