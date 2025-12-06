---
name: aoc-toolkit
description: API reference for jeffwindsor/aoc-toolkit Python library for Advent of Code puzzles. Use this skill when the user asks to use aoc-toolkit, or asks about reading input files, grids, coordinates, graph algorithms (bfs, dfs, dijkstra), or testing AoC solutions.
allowed-tools: Read, Grep, Glob
---

# AOC Toolkit Reference

Help the user with **syntax and API usage only**. Do not solve puzzles for them.

When the user asks "use aoc-toolkit to X", find the right function and show them how to use it.

## Quick Reference

| Task | Function | Example |
|------|----------|---------|
| Read lines | `read_data_as_lines` | `lines = read_data_as_lines("data/01")` |
| Parse grid | `read_data_as_char_grid` | `grid = read_data_as_char_grid("data/01")` |
| Read integers | `read_data_as_integers` | `nums = read_data_as_integers("data/01")` |
| Read coordinates | `read_data_as_coords` | `coords = read_data_as_coords("data/01")` |
| Read graph | `read_data_as_graph_edges` | `graph = read_data_as_graph_edges("data/01")` |
| Read sections | `read_data_as_sections` | `sections = read_data_as_sections("data/01")` |
| Navigate | `Coord` + directions | `pos = Coord(0, 0) + Coord.UP` |
| Find in grid | `find_first`, `find_all` | `start = find_first(grid, 'S')` |
| Grid coords | `grid_coords` | `for pos, val in grid_coords(grid):` |
| Grid path | `dfs_grid_path` | `path = dfs_grid_path(grid, start, end, walkable={'.', 'S', 'E'})` |
| BFS | `bfs` | `distances = bfs(start, neighbors_fn)` |
| DFS | `dfs` | `result = dfs(start, neighbors_fn)` |
| Dijkstra | `dijkstra` | `dist = dijkstra(start, neighbors_fn, goal=end)` |
| Max clique | `maximum_clique` | `clique = maximum_clique(graph)` |
| Test runner | `run`, `TestCase` | `run(solve, [TestCase("example")])` |

## Import Style

```python
from aoc import read_data_as_lines, Coord, bfs, run, TestCase
```

See [reference.md](reference.md) for full API details.
