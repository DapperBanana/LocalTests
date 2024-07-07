
import random

def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    def DFS(x, y):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx*2, y + dy*2
            
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '#':
                maze[nx][ny] = ' '
                maze[x + dx][y + dy] = ' '
                DFS(nx, ny)
    
    maze[0][1] = ' '
    DFS(0, 1)
    
    return maze

def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = [(0, 1)]
    parent = {}
    
    while queue:
        x, y = queue.pop(0)
        visited.add((x, y))
        
        if x == rows - 1 and y == cols - 2:
            path = []
            while (x, y) != (0, 1):
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append((0, 1))
            path.reverse()
            return path
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == ' ' and (nx, ny) not in visited:
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    
    return None

def print_maze(maze, path=None):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if path and (i, j) in path:
                print('.', end=' ')
            else:
                print(cell, end=' ')
        print()

rows, cols = 10, 20
maze = generate_maze(rows, cols)
path = solve_maze(maze)

print("Random maze:")
print_maze(maze)
print("\nSolution:")
print_maze(maze, path)
