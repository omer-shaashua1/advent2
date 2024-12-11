from pathlib import Path

# string_input = Path("G:\My Drive\Python Projects\input9.txt").read_text()

string_input = "2333133121414131402"
input_with_dots = ''


for i in range(len(string_input)):
    if i % 2 == 0:
        input_with_dots = input_with_dots + str(int(i/2)) * int(string_input[i])
    if i % 2 == 1:
        input_with_dots = input_with_dots + "." * int(string_input[i])

if input_with_dots == "00...111...2...333.44.5555.6666.777.888899":
    print("OK")

i, j = 0, len(input_with_dots)-1
edited_input = ''

while i <= j:
    while input_with_dots[i].isalnum():
        i += 1
    while not input_with_dots[j].isalnum():
        j -= 1



print(edited_input)
