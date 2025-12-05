from aoc import read_lines
from collections import Counter, defaultdict

sample=read_lines("data/04-sample.txt")
input_text=read_lines("data/04.txt")

def parse(lines: list) -> set[tuple[int, int]]:
    return {
        (r, c)
        for r, line in enumerate(lines)
        for c, ch in enumerate(line)
        if ch != '.'
    }

def count_neighbors(board:set[tuple[int,int]], pos):
    r,c = pos
    neighbors = set([(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1),(r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)])
    intersect = board.intersection(neighbors)
    return len(intersect)

def reachable_walls(board: set[tuple[int, int]]) -> set[tuple[int, int]]:
    neighbors = {pos: count_neighbors(board, pos) for pos in board}
    return {pos for pos in board if neighbors[pos] < 4}

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
