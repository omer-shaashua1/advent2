input_reports = list(open("input2.txt", "r"))


def check_level_diff(report: list):
    for i in range(len(report)-1):
        curr_level = int(report[i])
        next_level = int(report[i+1])
        if 0 == curr_level-next_level or abs(curr_level-next_level) >= 4 :
            return(False)
        return(True)



def report_fixer_step(report: list):
        for i in range(len(report)-1):
            curr_level = int(report[i])
            next_level = int(report[i+1])
            if 0 == curr_level-next_level or abs(curr_level-next_level) >= 4 :
                fixed_report = report
                fixed_report.pop(i)
                for j in range(len(fixed_report)-1):
                    fixed_curr_level = int(fixed_report[j])
                    fixed_next_level = int(fixed_report[j+1])
                    if 0 == fixed_curr_level-fixed_next_level or abs(fixed_curr_level-fixed_next_level) >= 4 :
                        fixed_report = report
                        fixed_report.pop(i)
                        for j in range(len(fixed_report)-1):
                            fixed_curr_level = int(fixed_report[j])
                            fixed_next_level = int(fixed_report[j+1])
                            if 0 == fixed_curr_level-fixed_next_level or abs(fixed_curr_level-fixed_next_level) >= 4 :
                                return(False)
                    return(True)
                return(True)
            return(True)

def report_fixer_monotonic(report: list):
    report_couples = zip(report, report[1:])
    for x,y in report_couples:
        if x > y:
            new_report = report
            new_report.remove(x)
            new_report_couples = zip(new_report, new_report[1:])
            for x,y in new_report_couples:
                if x > y:
                    new_report = report
                    new_report.remove(y)
                    new_report_couples = zip(new_report, new_report[1:])
                    for x,y in new_report_couples:
                        if x > y:
                            return(False)
                    return(True)
                return(True)
            return (new_report)
    return 3

def check_inc(list: list):
    return all(i < j for i, j in zip(list,list[1:]))


def check_dec(list: list):
    return all(i > j for i, j in zip(list,list[1:]))

def monotonic(list: list):
    return check_dec(list) or check_inc(list)

safe_levels=0

for j in range(len(input_reports)):
    split_level = input_reports[j].split()
    if report_fixer_step(split_level):
        safe_levels = safe_levels + 1

print(report_fixer_monotonic([1,2,3,4,5,3]))