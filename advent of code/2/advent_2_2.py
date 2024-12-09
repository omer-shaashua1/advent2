from pathlib import Path


# input_reports = open("input2.txt", "r").split()
input_reports = Path("G:\My Drive\Python Projects\input2.txt").read_text().split("\n")

def check_level_diff(report: list):
    for i in range(len(report)-1):
        curr_level = int(report[i])
        next_level = int(report[i+1])
        if 0 == curr_level-next_level or abs(curr_level-next_level) >= 4 :
            return(False)
    return(True)


def can_fix(report: list):
    for i in range(len(report)):
        fixed_report = report.copy()
        fixed_report.pop(i)
        if monotonic(fixed_report) and check_level_diff(fixed_report):
            return True
    return False



def check_inc(list: list):
    return all(i < j for i, j in zip(list,list[1:]))


def check_dec(list: list):
    return all(i > j for i, j in zip(list,list[1:]))

def monotonic(list: list):
    return check_dec(list) or check_inc(list)

safe_levels=0


for report in input_reports:
    split_report = report.split()
    if monotonic(split_report) and check_level_diff(split_report):
        safe_levels = safe_levels + 1
    elif can_fix(split_report):
        safe_levels = safe_levels + 1
    

print(safe_levels)

