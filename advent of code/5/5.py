from pathlib import Path
import re

rules_input = Path("G:\My Drive\Python Projects\input5_rules.txt").read_text().split()
updates_input = Path("G:\My Drive\Python Projects\input5_pages.txt").read_text().split()

#updates = []

# for idx in range(len(pages_input)):
#     pages.append(pages_input[idx].split(","))
                 


rules = {}

for rule in rules_input:
    split_rule = rule.split("|")
    if split_rule[0] in rules:
        rules[split_rule[0]].append(split_rule[1])
    else:
        rules[split_rule[0]] = [split_rule[1]]

def update_checker(update: list, rules: dict):
        for updated_page in updated_pages:
            try:
                for higher_page in rules[updated_page]:
                    if higher_page in updated_pages:
                        if updated_pages.index(updated_page) > updated_pages.index(higher_page):
                            return False
            except:
                 pass
        return True



sum_of_middles = 0
for update in updates_input:
     updated_pages = update.split(",")
    #  middle_of_page = updated_pages[]
     if update_checker(updated_pages, rules):
          sum_of_middles = sum_of_middles + int(updated_pages[int((len(updated_pages)-1)/2)])

print(sum_of_middles)


