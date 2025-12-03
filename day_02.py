from aoc import read_lines
from collections import Counter

sample=read_lines("data/02-sample.txt")
input_text=read_lines("data/02.txt")

def parse(lines:list)->list[tuple[int,int]]:
    line = lines[0]
    records=line.split(",")
    result = []
    for record in records:
        [low,high] = record.split("-")
        result.append((int(low), int(high)))
    return result

def is_invalid_id(value: int) -> bool:
    s = str(value)
    n = len(s)
    for size in range(1, n // 2 + 1):
        repeats = n // size
        if n % size: continue
        chunk = s[:size]
        if chunk * repeats == s:
            return True
    return False

def part1(pairs:list[tuple[int,int]])->int:
    count = 0
    x = 0
    for (low, high) in pairs:
        print(low, high)
        for i in range(low, high+1):
            if is_invalid_id(i):
                count += i
        x += 1
#        if x > 2: return 0
    return count

# def part2(commands:list[tuple[int,int]])->int:
#     return 0

#print("p1 sample: ", part1(parse(sample)))
#print("p1", part1(parse(input_text)))
print("p2 sample: ", part1(parse(sample)))
print("p2: ", part1(parse(input_text)))
