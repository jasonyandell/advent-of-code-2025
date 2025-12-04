from aoc import read_lines
from collections import Counter

sample=read_lines("data/03-sample.txt")
input_text=read_lines("data/03.txt")

def parse(lines:list)->list[list[int]]:
    return [[int(x) for x in line] for line in lines]

def max_joltage(nums:list[int], depth=12)->int:
    pos, total = 0, 0
    for remaining_choices in range(depth, 0, -1):
        # look at choices
        window = nums[pos:len(nums) - remaining_choices + 1]

        # find value and index of max choice
        value, next_index = max((v,i) for i, v in enumerate(window, pos))

        pos = next_index + 1 
        total = total * 10 + value

    return total


def part1(banks:list[list[int]])->int:
    result = 0
    for b in banks:
        #print(b, max_joltage(b))        
        result += max_joltage(b, 2)
    return result

def part2(banks:list[list[int]])->int:
    total = 0
    for b in banks:
        #print(b, max_joltage(b))        
        total += max_joltage(b)
    return total


print("p1 sample: ", part1(parse(sample)))
print("p1", part1(parse(input_text)))
print("p2 sample: ", part2(parse(sample)))
print("p2: ", part2(parse(input_text)))
