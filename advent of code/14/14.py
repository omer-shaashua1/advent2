from pathlib import Path
import re

# Create an input for the challenge. Each cell in machines has 3 values - button A, button B and the Prize
# challenge_input = Path("G:\My Drive\Python Projects\input14.txt").read_text().split("\n")
challenge_input = Path(r"G:\My Drive\Python Projects\test.txt").read_text().split("\n")

robots = []
map_size = (11,7)
robot_map = []
for line in range(map_size[1]):
    robot_map.append([])
    for row in range(map_size[0]):
        robot_map[line].append(0)

location_100sec = []

for robot in challenge_input:
    bot = re.split(r"p=|v=", robot)
    cleaned_bot = [value.strip() for value in bot if value]
    robots.append(cleaned_bot)

for robot in robots:
    robot[0] = robot[0].split(",")
    robot[1] = robot[1].split(",")

for robot in robots:
    location = [int(robot[0][0]), int(robot[0][1])]
    location_100sec.append([(location[0] + int(robot[1][0])*100) % len(robot_map[0]), (location[1] + int(robot[1][1])*100) % len(robot_map)])

# print(location_100sec)

for location in location_100sec:
    robot_map[location[1]][location[0]] = robot_map[location[1]][location[0]] + 1

sect1 = 0
sect2 = 0
sect3 = 0
sect4 = 0

for line_no in range(len(robot_map)//2):
    sect1 = sect1 + sum(robot_map[line_no][0:((len(robot_map[line_no])-1)//2)])

for line_no in range(len(robot_map)//2):
    sect2 = sect2 + sum(robot_map[line_no][((len(robot_map[line_no])+1)//2):])

for line_no in range((len(robot_map)+2)//2, len(robot_map)):
    sect3 = sect3 + sum(robot_map[line_no][0:((len(robot_map[line_no])-1)//2)])

for line_no in range((len(robot_map)+2)//2, len(robot_map)):
    sect3 = sect3 + sum(robot_map[line_no][((len(robot_map[line_no])+1)//2):])
    print(robot_map[line_no][((len(robot_map[line_no])+1)//2):])

# print(sect1)
# print(sect2)
# print(sect3)
# print(sect4)
x = range(4, 7)
print(x)

# for line in robot_map:
#     print(line)

# print(robots)
# print(test1)