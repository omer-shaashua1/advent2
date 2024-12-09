from pathlib import Path

rules_input = Path("G:\My Drive\Python Projects\input5_rules.txt").read_text().split()
updates_input = Path("G:\My Drive\Python Projects\input5_pages.txt").read_text().split()



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

def order_update(update_to_be_ordered: list, rules: dict):
    for updated_page in update_to_be_ordered:
        try:
            for higher_page in rules[updated_page]:
                if higher_page in update_to_be_ordered:
                    idx_page = update_to_be_ordered.index(updated_page)
                    idx_higher_page = update_to_be_ordered.index(higher_page)
                    if idx_page > idx_higher_page:
                        update_to_be_ordered[idx_page], update_to_be_ordered[idx_higher_page] = update_to_be_ordered[idx_higher_page], update_to_be_ordered[idx_page]
                        order_update(update_to_be_ordered, rules)
        except:
            pass
    return update_to_be_ordered

     


for update in updates_input:
     updated_pages = update.split(",")
    #  middle_of_page = updated_pages[]
     if not update_checker(updated_pages, rules):
        ordered = order_update(updated_pages, rules)
        if update_checker(ordered, rules):
            sum_of_middles = sum_of_middles + int(ordered[int((len(ordered)-1)/2)])


print(sum_of_middles)
