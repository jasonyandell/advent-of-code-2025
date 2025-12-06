# AOC Toolkit Full API Reference

## Installation

```bash
pip install git+https://github.com/jeffwindsor/aoc-toolkit.git@v1.0.1
```

---

## Data I/O (10 functions)

### read_data_as_lines(data_file: str) -> list[str]
Read file as list of lines.
```python
lines = read_data_as_lines("data/01")
```

### read_data_as_char_grid(data_file: str) -> list[list[str]]
Parse file into 2D character grid.
```python
grid = read_data_as_char_grid("data/01")
# grid[row][col] to access
```

### read_data_as_integers(data_file: str) -> list[int]
Extract all integers from file.
```python
nums = read_data_as_integers("data/01")
```

### read_data_as_coords(data_file: str) -> list[Coord]
Parse coordinate pairs from file.
```python
coords = read_data_as_coords("data/01")
```

### read_data_as_graph_edges(data_file: str) -> dict[str, list[str]]
Parse graph as adjacency list.
```python
graph = read_data_as_graph_edges("data/01")
# graph["A"] -> ["B", "C"]
```

### read_data_as_sections(data_file: str) -> list[list[str]]
Split file by blank lines into sections.
```python
sections = read_data_as_sections("data/01")
# sections[0] = first block of lines
# sections[1] = second block after blank line
```

---

## Coord Class

### Coord(row: int, col: int)
Immutable 2D coordinate.

```python
from aoc import Coord

pos = Coord(0, 0)
pos.row  # 0
pos.col  # 0
```

### Direction Constants
```python
Coord.UP        # (-1, 0)
Coord.DOWN      # (1, 0)
Coord.LEFT      # (0, -1)
Coord.RIGHT     # (0, 1)
Coord.UP_LEFT   # (-1, -1)
Coord.UP_RIGHT  # (-1, 1)
Coord.DOWN_LEFT # (1, -1)
Coord.DOWN_RIGHT# (1, 1)

Coord.DIRECTIONS_CARDINAL  # [UP, DOWN, LEFT, RIGHT]
Coord.DIRECTIONS_DIAGONAL  # [UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]
Coord.DIRECTIONS_ALL       # all 8 directions
```

### Movement
```python
new_pos = pos + Coord.UP      # move up
new_pos = pos + Coord(2, 3)   # add coordinates
```

### Methods
```python
pos.manhattan_distance(other)  # |row1-row2| + |col1-col2|
pos.in_bounds(rows, cols)      # True if 0 <= row < rows and 0 <= col < cols
pos.neighbors()                # list of 4 cardinal neighbors
pos.neighbors_all()            # list of 8 neighbors (including diagonal)
```

---

## Grid Operations (12 functions)

### find_first(grid, value) -> Coord | None
Find first occurrence of value in grid.
```python
start = find_first(grid, 'S')
```

### find_all(grid, value) -> list[Coord]
Find all occurrences of value in grid.
```python
walls = find_all(grid, '#')
```

### grid_coords(grid) -> Iterator[tuple[Coord, value]]
Iterate through all coordinates and values.
```python
for pos, val in grid_coords(grid):
    if val == 'X':
        print(pos)
```

### dfs_grid_path(grid, start, end, walkable_values) -> list[Coord] | None
Find path through grid using DFS.
```python
path = dfs_grid_path(grid, start, end, walkable_values={'.', 'S', 'E'})
if path:
    print(f"Path length: {len(path) - 1}")
```

---

## Graph Algorithms

### bfs(start, neighbors_fn, goal=None) -> dict | int
Breadth-first search. Returns distances dict, or distance to goal if specified.
```python
def neighbors(node):
    return [n for n in graph[node]]

distances = bfs(start, neighbors)
# distances[node] = steps from start

# Or find specific goal:
dist = bfs(start, neighbors, goal=end)
```

### dfs(start, neighbors_fn) -> set
Depth-first search. Returns all reachable nodes.
```python
reachable = dfs(start, neighbors)
```

### dijkstra(start, neighbors_fn, goal=None) -> dict | int
Shortest path with weighted edges.
```python
def neighbors(node):
    # Return list of (neighbor, cost) tuples
    return [(n, weight) for n, weight in graph[node]]

distances = dijkstra(start, neighbors)
# Or:
dist = dijkstra(start, neighbors, goal=end)
```

### maximum_clique(graph) -> set
Find largest fully-connected subgraph.
```python
clique = maximum_clique(graph)
```

---

## Testing

### TestCase(name: str)
Define a test case. Auto-loads expected answer from `{name}.part1.answer` or `{name}.part2.answer`.

### run(solve_fn, test_cases, part="part1")
Run solution against test cases with colored output.

```python
from aoc import run, TestCase

def solve(data_file):
    lines = read_data_as_lines(data_file)
    # solve puzzle
    return answer

if __name__ == "__main__":
    run(solve, [
        TestCase("example_01"),
        TestCase("puzzle_input"),
    ], part="part1")
```

### Expected File Structure
```
project/
├── solution.py
└── data/
    ├── example_01
    ├── example_01.part1.answer
    ├── puzzle_input
    └── puzzle_input.part1.answer
```

---

## Math Utilities

### count_segments(values) -> int
Count continuous segments in sequence.

### count_digits(n) -> int
Count digits in integer.
