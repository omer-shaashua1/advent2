input_lists = open("input1.txt", "r")

list_1 = []
list_2 = []
list_of_places = list(input_lists)
for i in list_of_places:
    split_list = i.split()
    list_1.append(int(split_list[0]))
    list_2.append(int(split_list[1]))

#sorted_list_1 = list_1.sort()
#sorted_list_2 = list_2.sort()

diff_value = 0

#for i in range(len(list_1)):
#    diff = abs(list_1[i]-list_2[i])
#    diff_sum = diff_sum + diff

for i in range(len(list_1)):
    mult = list_2.count(list_1[i])
    diff_value = diff_value + list_1[i] * mult



print(diff_value)