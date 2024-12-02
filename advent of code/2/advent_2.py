input_reports = list(open("input2.txt", "r"))




def check_level_diff(list: list):
    for i in range(len(list)-1):
        if 0 == abs(int(list[i])-int(list[i+1])) or abs(int(list[i])-int(list[i+1])) >= 4 :
            return(0)
    return(1)


def check_increase(list: list):
    for i in range(len(list)-1):
        if int(list[i]) < int(list[i+1]):
            i = i + 1
        else:
            return(0)
    return(1)

def check_decrease(list: list):
    for i in range(len(list)-1):
        if int(list[i]) > int(list[i+1]):
            i = i + 1
        else:
            return(0)
    return(1)

safe_levels = 0

for i in range(len(input_reports)):
    split_level = input_reports[i].split()
    if check_level_diff(split_level) == 1:
        if check_increase(split_level) == 1 or check_decrease(split_level) == 1:
            safe_levels = safe_levels + 1
        
        

print(safe_levels)
