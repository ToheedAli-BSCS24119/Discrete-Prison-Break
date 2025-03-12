import os
from collections import deque

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Define the grid
grid = [
    ['S', 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 'E']
]

# Directions for moving (right, left, down, up)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Find start and end positions
def find_positions(grid):
    start = end = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)
    return start, end

# BFS to find shortest path
def bfs(grid):
    start, end = find_positions(grid)
    if not start or not end:
        return "Invalid grid: Missing 'S' or 'E'"

    queue = deque([(start[0], start[1], 0, [start])])  # (row, col, steps, path)
    visited = set()
    visited.add(start)

    while queue:
        r, c, steps, path = queue.popleft()

        if (r, c) == end:
            path_str = " -> ".join([f"({x}, {y})" for x, y in path])
            return f"Shortest path found in {steps+1} steps!\nPath: {path_str}"

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 1 and (nr, nc) not in visited:
                queue.append((nr, nc, steps + 1, path + [(nr, nc)]))
                visited.add((nr, nc))

    return "No path found!"

# Run BFS and print the result
print(bfs(grid))
