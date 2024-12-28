
import random

def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if random.random() < 0.3:
                maze[i][j] = ' '

    maze[0][1] = ' '
    maze[rows-1][cols-2] = ' '
    
    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

def find_path(maze, start, end):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    stack = [start]
    parent = {start: None}
    
    while stack:
        current = stack.pop()
        
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        visited.add(current)
        
        for di, dj in directions:
            new_i, new_j = current[0] + di, current[1] + dj
            if 0 <= new_i < len(maze) and 0 <= new_j < len(maze[0]) and maze[new_i][new_j] != '#' and (new_i, new_j) not in visited:
                stack.append((new_i, new_j))
                parent[(new_i, new_j)] = current
                
    return []

rows = 10
cols = 10

maze = generate_maze(rows, cols)
print("Random Maze:")
print_maze(maze)

start = (0, 1)
end = (rows-1, cols-2)

path = find_path(maze, start, end)
if path:
    print("\nSolution:")
    for i, j in path:
        maze[i][j] = 'X'
    print_maze(maze)
else:
    print("\nNo solution found.")
