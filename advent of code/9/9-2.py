from pathlib import Path

# string_input = Path(r"C:\Users\user 1\Downloads\python\advent2\input9.txt").read_text()
string_input = "2333133121414131402"


input_with_dots = []

for i in range(len(string_input)):
    if i % 2 == 0:
        list_to_add = [str(int(i/2))] * int(string_input[i])
        input_with_dots += list_to_add
    if i % 2 == 1:
        list_to_add = ["."] * int(string_input[i])
        input_with_dots += list_to_add


def find_gap(input_list: list, current_location: int):
    while input_list[current_location].isalnum():
        current_location += 1
    gap_start = current_location
    while input_list[current_location] == '.':
        current_location += 1
    gap_end = current_location
    gap_size = gap_end - gap_start
    return gap_start, gap_end, gap_size


def find_file(input_list: list, current_location: int):
    while input_list[current_location] == '.':
        current_location -= 1
    file_start = current_location
    while input_list[current_location] == input_list[current_location-1]:
        current_location -= 1
    file_end = current_location - 1
    file_size = file_start - file_end
    return file_start, file_end, file_size


def move_file(input_list:list, gap_start: int, file_start: int, file_size:int):
    for spot in range(file_size):
        input_list[gap_start+spot], input_list[file_start-file_size+1+spot] = input_list[file_start-file_size+1+spot], input_list[gap_start+spot]

changes_made = 1
while changes_made != 0:
    changes_made = 0
    i, j = 0, len(input_with_dots)-1
    gap_start, i, gap_size = find_gap(input_with_dots, i)
    file_start, j, file_size = find_file(input_with_dots, j)
    while gap_size < file_size and j > 0:
        file_start, j, file_size = find_file(input_with_dots, j)
    if gap_size >= file_size:
        move_file(input_with_dots, gap_start, file_start, file_size)
        changes_made += 1


# i, j = 0, len(input_with_dots)-1
# while i <= j:
#     while i < len(input_with_dots)-1 and input_with_dots[i] != ".":
#         i += 1
#     gap_start = i
#     while i < len(input_with_dots)-1 and input_with_dots[i] == '.':
#         i += 1
#     gap_end = i
#     while input_with_dots[j] == '.':
#         j -= 1
#     file_start = j
#     while input_with_dots[j-1] == input_with_dots[j]:
#         j -= 1
#     file_end = j-1

#     gap_size = gap_end - gap_start
#     file_size = abs(file_end - file_start)

#     if gap_size >= file_size:
#         for spot in range(file_size):
#             input_with_dots[i-gap_size+spot], input_with_dots[j+spot] = input_with_dots[j+spot], input_with_dots[i-gap_size+spot]



print(input_with_dots)
print(find_file(input_with_dots, 41))

checksum = 0
for idx, char in enumerate(input_with_dots):
    if char.isnumeric():
        checksum = checksum + (idx * int(char))

print("checksum =", checksum)
