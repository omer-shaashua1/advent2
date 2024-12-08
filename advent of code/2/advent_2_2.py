input_reports = list(open("input2.txt", "r"))


def check_level_diff(report: list):
    for i in range(len(report)-1):
        curr_level = int(report[i])
        next_level = int(report[i+1])
        if 0 == curr_level-next_level or abs(curr_level-next_level) >= 4 :
            return(False)
        return(True)


def report_step_checker(report: list):
    for i in range(len(report)-1):
        curr_level = int(report[i])
        next_level = int(report[i+1])
        if 0 == curr_level-next_level or abs(curr_level-next_level) >= 4:
            return(i)
    return(True)


def step_fixer_idx(report: list, idx: int):
    new_report = report.copy()
    new_report.pop(idx)
    if report_step_checker(new_report):
        return(new_report)
    return(False)
    

def step_fixed_after_idx(report: list, idx: int):
    new_report = report.copy()
    new_report.pop(idx+1)
    if report_step_checker(new_report):
        return(new_report)
    return(False)


def mon_inc(report: list):
    report_couples = zip(report, report[1:])
    for x,y in report_couples:
        if x > y:
            return report.index(x)
    return(True)


def mon_dec(report: list):
    report_couples = zip(report, report[1:])
    for x,y in report_couples:
        if x < y:
            return report.index(x)
    return(True)


def monotonicity_fixer_idx(report: list, idx: int):
    new_report = report.copy()
    new_report.pop(idx)
    if monotonic(new_report):
        return(new_report)
    return(False)


def monotonicity_fixer_after_idx(report: list, idx:int):
    new_report = report.copy()
    new_report.pop(idx+1)
    if monotonic(new_report):
        return(new_report)
    return(False)


def check_direction(report: list):
    step_inc = 0
    step_dec = 0
    report_couples = zip(report, report[1:])
    for x,y in report_couples:
        if x < y:
            step_inc = step_inc + 1
        if x > y: 
            step_dec = step_dec + 1
        if step_dec == 1:
            return("inc")
        if step_inc == 1:
            return("dec")
    return(False)



    
# for j in range(len(input_reports)):
#     split_level = input_reports[j].split()
#     if report_step_checker(split_level):
#         if monotonic(split_level):
#             safe_levels = safe_levels + 1
#         edited_report = monotonicity_fixer_idx(split_level, mon_inc)
#         if edited_report




# def report_fixer_monotonic(report: list):
#     report_couples = zip(report, report[1:])
#     for x,y in report_couples:
#         if x > y:
#             new_report = report
#             new_report.remove(x)
#             new_report_couples = zip(new_report, new_report[1:])
#             for x,y in new_report_couples:
#                 if x > y:
#                     new_report = report
#                     new_report.remove(y)
#                     new_report_couples = zip(new_report, new_report[1:])
#                     for x,y in new_report_couples:
#                         if x > y:
#                             return(False)
#                     return(True)
#                 return(True)
#             return (new_report)
#     return 3

def check_inc(list: list):
    return all(i < j for i, j in zip(list,list[1:]))


def check_dec(list: list):
    return all(i > j for i, j in zip(list,list[1:]))

def monotonic(list: list):
    return check_dec(list) or check_inc(list)

safe_levels=0



# for j in range(len(input_reports)):
#     split_level = input_reports[j].split()
#     if report_step_checker(split_level):
#         if monotonic(split_level):
#             safe_levels = safe_levels + 1
#         edited_report = monotonicity_fixer_idx(split_level, mon_inc)
#         if edited_report

# for j in range(len(input_reports)):
#     split_level = input_reports[j].split()
#     if report_fixer_step(split_level):
#         safe_levels = safe_levels + 1

test_report = [1, 2, 3, 5, 7, 2]
test_idx = report_step_checker(test_report)

#print(step_fixer(test_report, test_idx))

# if "int"=="int":
#     print(1)