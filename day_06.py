from aoc import read_data
import re
from collections import Counter
from functools import reduce

sample=read_data("06-sample.txt").splitlines()
input_text=read_data("06.txt").splitlines()

type Column = tuple[str, list[int]]

def parse1(lines:list[str])->list[Column]:
    result:list[list[int]] = []
    operators:list[str] = []
    for line in lines:
        stripped = re.sub(r'\s+', ' ', line).strip().split(' ')
        if any(c in stripped for c in '+*'):
            operators = stripped
        else:
            result.append([int(x) for x in stripped])
    number_columns:list[list[int]] = [list(transposed) for transposed in zip(*result)]
    final = list(zip(operators, number_columns))
    return final

def part1(columns:list[Column])->int:
    total = 0
    for operator, data in columns:
        if (operator == '+'):
            total += reduce(lambda acc, x:acc + x, data)
        else:
            total += reduce(lambda acc, x:acc * x, data)
    return total

def parse2(raw_lines:list[str])->list[Column]:
    lines = [list(line) for line in raw_lines]
    block_starts = [i for i,c in enumerate(lines[-1]) if c != ' ']+[len(lines[0])]
    blocks:list[list[int]] = []
    for idx,_ in enumerate(block_starts[:-1]):
        block = [l[block_starts[idx]:block_starts[idx+1]] for l in lines[:-1]]
        # print(block)
        values:list[int] = []
        for col in range(len(block[0])):
            row = (''.join([row[col] for row in block])).strip()
            if (row != ''): values.append(int(row))
            # print(row)
        blocks.append(values)
    
    operators = [raw_lines[-1][idx] for idx in block_starts[:-1]]
    final = list(zip(operators, blocks))

    return final

print("p1 sample: ", part1(parse1(sample)))
print("p1", part1(parse1(input_text)))
print("p2 sample: ", part1(parse2(sample)))
print("p2: ", part1(parse2(input_text)))
