from aoc import read_lines
from collections import Counter

part1_sample=read_lines("data/01-sample.txt")
part1_text=read_lines("data/01.txt")

def parse(lines:list)->list[tuple[str, int]]:
    result = []
    for line in lines:
        instruction = line[0]
        value = int(line[1:])
        result.append((instruction, value))
    return result

def part1(commands:list[tuple[str, int]]):
    pos = 50
    zeroes = 0
    for (direction, value) in commands:
        if (direction == "L"): pos = pos - value
        else: pos = pos + value
        pos = (pos + 1000000000) % 100
        if pos == 0: zeroes += 1

    return zeroes

def move(direction:str, pos:int)->int:
    if (direction=="L"):
        pos -= 1
    else:
        pos += 1
    return (pos + 1000000) % 100

def part2(commands:list[tuple[str, int]]):
    pos = 50
    zeroes = 0
    for (direction, value) in commands:
        for i in range(value):
            pos = move(direction, pos)            
            if pos == 0: zeroes += 1

    return zeroes

print("p1 sample: ", part1(parse(part1_sample)))
print("p1", part1(parse(part1_text)))
print("p2 sample: ", part2(parse(part1_sample)))
print("p2: ", part2(parse(part1_text)))
