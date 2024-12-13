from pathlib import Path

string_input = Path(r"C:\Users\user 1\Downloads\python\advent2\input9.txt").read_text()
# string_input = "2333133121414131402"


input_with_dots = []

for i in range(len(string_input)):
    if i % 2 == 0:
        list_to_add = [str(int(i/2))] * int(string_input[i])
        input_with_dots += list_to_add
    if i % 2 == 1:
        list_to_add = ["."] * int(string_input[i])
        input_with_dots += list_to_add


i, j = 0, len(input_with_dots)-1
while i <= j:
    while i < len(input_with_dots) and input_with_dots[i] != ".":
        i = i + 1
    while input_with_dots[j] == '.':
        j = j - 1
    if i <= j:
        input_with_dots[i], input_with_dots[j] = input_with_dots[j], input_with_dots[i]



checksum = 0
for idx, char in enumerate(input_with_dots):
    if char.isnumeric():
        checksum = checksum + (idx * int(char))

print("checksum =", checksum)
