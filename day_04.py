from aoc import read_lines
from collections import Counter, defaultdict

sample=read_lines("data/04-sample.txt")
input_text=read_lines("data/04.txt")

def parse(lines:list)->set[tuple[int,int]]:
    x = set()
    for (r,line) in enumerate(lines):
        for (c, curr) in enumerate(line):
            if (curr != '.'):
                x.add((r,c))
    return x


def count_neighbors(board:set[tuple[int,int]], pos):
    r,c = pos
    neighbors = set([(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1),(r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)])
    intersect = board.intersection(neighbors)
    return len(intersect)

def reachable_walls(board:set[tuple[int,int]])->set[tuple[int,int]]:
    map: defaultdict[tuple[int,int], int] = defaultdict(int) 
    for pos in board:
        map[pos] = count_neighbors(board, pos)
    filtered = set([pos for pos in board if map[pos] >= 4])
    remaining = board - filtered
    return remaining

def part1(board:set[tuple[int,int]])->int:
    return len(reachable_walls(board))

def part2(board: set[tuple[int, int]]) -> int:
    removed = 0
    while reachable := reachable_walls(board):
        removed += len(reachable)
        board -= reachable
    return removed

print("p1 sample: ", part1(parse(sample)))
print("p1", part1(parse(input_text)))
print("p2 sample: ", part2(parse(sample)))
print("p2: ", part2(parse(input_text)))
