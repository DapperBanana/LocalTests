
import random

def generate_maze(n, m):
    maze = [['#' for _ in range(m)] for _ in range(n)]
    
    for i in range(1, n, 2):
        for j in range(1, m, 2):
            maze[i][j] = ' '
    
    stack = [(1, 1)]
    
    while stack:
        x, y = stack[-1]
        maze[x][y] = ' '
        
        neighbors = []
        if x > 2 and maze[x - 2][y] == '#':
            neighbors.append((x - 2, y))
        if x < n - 2 and maze[x + 2][y] == '#':
            neighbors.append((x + 2, y))
        if y > 2 and maze[x][y - 2] == '#':
            neighbors.append((x, y - 2))
        if y < m - 2 and maze[x][y + 2] == '#':
            neighbors.append((x, y + 2))
        
        if neighbors:
            neighbor = random.choice(neighbors)
            nx, ny = neighbor
            maze[(x + nx) // 2][(y + ny) // 2] = ' '
            stack.append(neighbor)
        else:
            stack.pop()
    
    return maze

def solve_maze(maze):
    def dfs(x, y):
        if maze[x][y] == ' ':
            maze[x][y] = '*'
            if x == len(maze) - 2 and y == len(maze[0]) - 2:
                return True
            if x > 1 and dfs(x - 2, y):
                return True
            if x < len(maze) - 2 and dfs(x + 2, y):
                return True
            if y > 1 and dfs(x, y - 2):
                return True
            if y < len(maze[0]) - 2 and dfs(x, y + 2):
                return True
            maze[x][y] = ' '
        
        return False
    
    dfs(1, 1)
    
    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

n = 11
m = 11

maze = generate_maze(n, m)
print("Generated maze:")
print_maze(maze)

print("\nSolved maze:")
solved_maze = solve_maze(maze)
print_maze(solved_maze)
