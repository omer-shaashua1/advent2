from pathlib import Path

# string_input = Path("G:\My Drive\Python Projects\input9.txt").read_text()
string_input = "2333133121414131402"
input_with_dots = ''


for i in range(len(string_input)):
    if i % 2 == 0:
        input_with_dots = input_with_dots + str(int(i/2)) * int(string_input[i])
    if i % 2 == 1:
        input_with_dots = input_with_dots + "." * int(string_input[i])

input_list = list(input_with_dots)

i, j = 0, len(input_with_dots)-1
while i < j:
    while i < len(input_list) and input_list[i] != ".":
        i += 1
    while input_list[j] == '.':
        j -= 1
    if i < j:
        input_list[i], input_list[j] = input_list[j], input_list[i]


sum_of_org = 0
for idx, char in enumerate(input_list):
    if char.isalnum():
        sum_of_org += idx * int(char)

print(sum_of_org)
