input_reports = list(open("input2.txt", "r"))


def check_level_diff(report: list):
    for i in range(len(report)-1):
        curr_level = int(report[i])
        next_level = int(report[i+1])
        if 0 == curr_level-next_level or abs(curr_level-next_level) >= 4 :
            fixed_report = report.pop(i)
            for j in range(len(fixed_report)-1):
                fixed_curr_level = int(fixed_report[j])
                fixed_next_level = int(fixed_report[j+1])
                if 0 == fixed_curr_level-fixed_next_level or abs(fixed_curr_level-fixed_next_level) >= 4 :
                    fixed_report = report.pop(i+1)
                    for j in range(len(fixed_report)-1):
                        fixed_curr_level = int(fixed_report[j])
                        fixed_next_level = int(fixed_report[j+1])
                        if 0 == fixed_curr_level-fixed_next_level or abs(fixed_curr_level-fixed_next_level) >= 4 :
                            return(0)
                    else:
                        if monotonic(fixed_report):
                            return(1)
                else:
                    if monotonic(fixed_report):
                        return(1)
        else:
            if monotonic(report):
                return(1)
        return(0)


# def check_level_diff(report: list):
#     for i in range(len(report)-1):
#         if 0 < abs(int(report[i])-int(report[i+1])) < 4 :
#             i = i + 1
#         else:
#             fixed_report = report.pop(i)
#             for j in range(len(fixed_report)-1):
#                 if 0 < abs(int(list[i])-int(list[i+1])) < 4 :
#                 j = j + 1
#             if monotonic(fixed_report):
#                 return (1)
#             else: 
#                 fixed_report = report.pop(i+1)
#                 if monotonic(fixed_report):
#                     return(1)
#             return(0)
#     return(1)

def check_inc(list: list):
    return all(i < j for i, j in zip(list,list[1:]))


def check_dec(list: list):
    return all(i > j for i, j in zip(list,list[1:]))

def monotonic(list: list):
    return check_dec(list) or check_inc(list)

safe_levels=0

for i in range(len(input_reports)):
    split_level = input_reports[i].split()
    if check_level_diff(split_level) == 1:
        safe_levels = safe_levels + 1

print(safe_levels)
