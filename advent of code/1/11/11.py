from pathlib import Path

start_stones = Path("G:\My Drive\Python Projects\input11.txt").read_text().split()
# start_stones = ["125", "17"]
# print(start_stones)

def even_blink(stone: str):
    split_stone = (str(int(stone[0:int(len(stone)/2)])), str(int(stone[int(len(stone)/2):])))
    return split_stone

def odd_stone(stone: str):
    blinked_stone = str(int(stone) * 2024)
    return blinked_stone


i = 0
number_of_blinks = 75
while i < number_of_blinks:
    blinked = []
    for stone in start_stones:
        if len(stone) % 2 == 0:
            blinked.append(even_blink(stone)[0])
            blinked.append(even_blink(stone)[1])
        elif stone == "0":
            blinked.append("1")
        elif len(stone) % 2 == 1:
            blinked.append(odd_stone(stone))
    start_stones = blinked.copy()
    i += 1


print(len(start_stones))

