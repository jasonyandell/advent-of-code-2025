from helpers import read_lines
from collections import Counter

sample=read_lines("data/05-sample.txt")
input_text=read_lines("data/05.txt")

def parse(lines:list[str])->tuple[list[tuple[int,int]], list[int]]:
    ranges:list[tuple[int,int]] = []
    checks:list[int] = []
    result = (ranges, checks)
    for line in lines:
        if line=='':
            continue
        elif line.isnumeric():
            checks.append(int(line))
        else:
            [start, end] = line.split('-')
            ranges.append((int(start), int(end)))
    return result


def merge_intervals(ranges:list[tuple[int,int]])->list[tuple[int,int]]:
    if not ranges:
        return []
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    result = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = result[-1]
        if start <= last_end + 1:  # overlapping or adjacent
            result[-1] = (last_start, max(last_end, end))
        else:
            result.append((start, end))
    return result

def in_range(check:int, ranges:list[tuple[int,int]])->bool:
    for (lo, hi) in ranges:
        if lo <= check <= hi: return True
    return False 

def part1(problem: tuple[list[tuple[int,int]], list[int]])->int:
    (ranges, checks) = problem
    compact = merge_intervals(ranges)
    # print(compact)
    count = 0
    for check in checks:
        if in_range(check, compact): count += 1
    return count

def part2(problem: tuple[list[tuple[int,int]], list[int]])->int:
    (ranges, _) = problem
    merged = merge_intervals(ranges)
    total = 0
    for (lo, hi) in merged:
        total += hi - lo + 1
    return total

print("p1 sample: ", part1(parse(sample)))
print("p1", part1(parse(input_text)))
print("p2 sample: ", part2(parse(sample)))
print("p2: ", part2(parse(input_text)))
